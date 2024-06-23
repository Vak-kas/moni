import logging
from classify.models import WordCount, FullSentence, Hosts, Normal, Casino, Adult, Copyright
from konlpy.tag import Okt
from collections import Counter
from asgiref.sync import sync_to_async
import random

# 로깅 설정
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# 형태소 분석기 객체 생성
okt = Okt()

# FullSentence 테이블의 문장을 분석하고 WordCount 테이블에 저장하는 함수
async def analyze_and_store_full_sentence(host):
    logger.debug(f"Analyzing and storing full sentences for host: {host}")
    full_sentences = await sync_to_async(list)(
        FullSentence.objects.filter(host=host).values_list('full_sentence', flat=True))

    word_count = Counter()
    for sentence in full_sentences:
        words = okt.nouns(sentence)
        word_count.update(words)

    for word, count in word_count.items():
        await sync_to_async(WordCount.objects.create)(
            host=host,
            words=word,
            count=count
        )
    logger.debug("Finished analyzing and storing full sentences")

# 단어를 카테고리별 테이블에 저장하는 함수
async def save_keywords_to_category_tables():
    logger.debug("Saving keywords to category tables")

    categories = {
        "정상": Normal,
        "도박사이트": Casino,
        "성인사이트": Adult,
        "불법저작물배포사이트": Copyright
    }

    for category, model in categories.items():
        # 기존 단어 삭제
        await sync_to_async(model.objects.all().delete)()

        words = await sync_to_async(list)(
            WordCount.objects.filter(host__classification=category).values_list('words', flat=True)
        )
        if words:
            most_common_words = [word for word, _ in Counter(words).most_common(70)] #가장 많은 단어 70개 가져오기
            remaining_words = list(set(words) - set(most_common_words))
            random_words = random.sample(remaining_words, min(30, len(remaining_words))) #30개 랜덤으로 가져옹니
            combined_words = most_common_words + random_words

            for word in combined_words:
                await sync_to_async(model.objects.create)(word=word)

    logger.debug("Finished saving keywords to category tables")