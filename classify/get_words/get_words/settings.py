import os
import sys
import django

# Django 프로젝트의 루트 디렉토리 경로를 추가
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '..', '..'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

django.setup()

BOT_NAME = 'get_words'

SPIDER_MODULES = ['get_words.spiders']
NEWSPIDER_MODULE = 'get_words.spiders'

ROBOTSTXT_OBEY = False

# Enable rotating proxies
# PROXY_POOL_ENABLE = False
# PROXY_POOL_PAGE_RETRY_TIMES = 5
# PROXY_POOL_TRY_WITH_HOST = False
# HTTPERROR_ALLOWED_CODES = [403]

# Downloader middlewares settings
DOWNLOADER_MIDDLEWARES = {
#     # 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': 700,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware' : 400,
#     # 'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
#     # 'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 550,  # 우선순위 높이기
}

# Retry settings
RETRY_ENABLED = True
RETRY_TIMES = 1  # 기본값은 2입니다. 필요한 경우 더 낮출 수 있습니다.
RETRY_HTTP_CODES = [500, 502, 503, 504, 522, 524, 408, 429, 403]  # 필요한 경우 추가 HTTP 코드
RETRY_PRIORITY_ADJUST = -1  # 낮은 우선순위로 재시도

# Timeout settings
DOWNLOAD_TIMEOUT = 2  # 기본값은 180초입니다. 필요에 따라 조절하세요.

# 직접 프록시 리스트 작성
ROTATING_PROXY_LIST = [
    '84.252.73.132:4444',
    '62.236.76.83:8085',
    '91.92.155.207:3128',
    '72.10.164.178:25371',
    '65.109.179.27:80',
    '65.109.189.49:80',
    '125.77.25.178:8090',
    '34.148.178.57:4444',
    '64.227.4.244:8888',
    '67.43.236.19:3397',
    '67.43.236.20:31979',
    '125.77.25.177:8080',
    '185.105.91.62:4444',
    '51.158.169.52:29976',
    '47.56.110.204:8989',
    '91.107.147.205:80',
    '139.162.78.109:8080',
    '111.160.204.146:9091',
    '185.222.115.104:31280',
    '188.132.209.245:80',
    '67.43.227.226:32847',
    '20.235.159.154:80',
    '135.181.154.225:80',
    '72.10.164.178:5313',
    '51.195.40.90:80',
    '221.140.235.236:5002',
    '152.26.229.86:9443',
    '72.10.160.171:8465',
    '35.185.196.38:3128',
    '203.57.51.53:80',
    '103.86.109.38:80',
    '51.89.14.70:80',
    '51.254.78.223:80',
    '12.186.205.122:80',
    '154.85.58.149:80',
    '103.49.202.252:80',
    '185.105.89.249:4444',
    '79.174.12.190:80',
    '103.198.26.22:80',
    '34.23.45.223:80',
    '72.10.160.90:21403',
    '203.89.8.107:80',
    '123.30.154.171:7777',
    '51.89.73.162:80',
    '51.178.142.1:80',
    '51.210.107.197:3128',
    '51.210.19.141:80',
    '161.35.70.249:8080',
    '67.43.228.253:28521',
    '67.43.227.227:22443',
    '223.113.80.158:9091',
    '54.38.181.125:80',
    '51.255.0.233:80',
    '202.55.67.194:80',
    '65.109.204.150:80',
    '178.48.68.61:18080',
    '72.10.164.178:1991',
    '84.252.74.190:4444',
    '84.252.75.136:4444',
    '198.44.255.5:80',
    '178.128.113.118:23128',
    '72.10.160.171:26787',
    '185.232.169.108:4444',
    '43.153.75.22:80',
    '120.197.160.2:9002',
    '183.221.221.149:9091',
    '62.162.90.212:80',
    '198.49.68.80:80',
    '125.77.25.178:8080',
    '8.213.151.128:3128',
    '67.227.240.157:3128',
    '67.43.227.227:2003',
    '159.69.86.130:80',
    '103.153.154.6:80',
    '47.89.184.18:3128',
    '183.234.215.11:8443',
    '154.49.246.35:80',
    '67.43.236.18:21729',
    '185.105.90.88:4444',
    '67.43.227.227:32829',
    '213.217.30.69:3128',
    '13.81.217.201:80',
    '49.13.9.253:80',
    '91.189.177.190:3128',
    '125.77.25.177:8090',
    '189.240.60.166:9090',
    '67.43.236.20:24007',
    '185.222.115.66:31280',
    '119.39.109.233:3128',
    '38.91.101.96:8850',
    '72.10.160.172:17293',
    '139.59.1.14:8080',
    '67.43.236.20:31543',
    '89.116.191.51:80',
    '183.238.163.8:9002',
    '104.194.152.35:34567',
    '47.74.152.29:8888',
    '47.243.92.199:3128',
    '34.175.101.255:80',
    '54.38.181.125:3128',
    '72.10.164.178:27361',
    '47.242.47.64:8888',
    '37.120.189.106:80',
    '147.45.104.252:80',
    '152.26.229.42:9443',
    '67.43.236.18:5579',
    '45.9.75.76:4444',
    '216.137.184.253:80',
    '189.240.60.171:9090',
    '51.210.223.9:3000',
    '203.205.9.105:8080',
    '219.129.167.82:2222',
    '203.19.38.114:1080',
    '154.203.132.49:8090',
    '91.189.177.189:3128',
    '185.217.198.121:4444',
    '51.161.56.52:80',
    '185.105.88.63:4444',
    '67.43.227.227:30791',
    '84.39.112.144:3128',
    '213.218.228.253:80',
    '49.13.48.21:80',
    '162.55.40.2:80',
    '67.43.228.253:2365',
    '133.18.234.13:80',
    '67.43.228.250:30835',
    '103.156.17.41:8818',
    '185.105.91.53:4444',
    '128.199.202.122:8080',
    '47.236.72.111:10801',
    '67.43.236.20:31429',
    '45.22.209.157:8888',
    '5.161.103.113:80',
    '93.127.163.52:80',
    '94.228.163.140:80',
    '183.215.23.242:9091',
    '198.44.255.3:80',
    '182.70.114.56:3128',
    '47.91.104.88:3128',
    '46.249.99.103:80',
    '117.54.114.98:80',
    '198.74.51.79:8888',
    '172.183.241.1:8080',
    '195.35.2.231:80',
    '72.10.164.178:18027',
    '72.10.160.94:18661',
    '139.59.1.14:3128',
    '72.10.160.90:7061',
    '104.194.152.30:34567',
    '38.188.249.104:8181',
    '167.102.133.105:80',
    '41.231.37.76:3128',
    '51.210.127.15:80',
    '135.125.248.252:80',
    '199.167.236.12:3128',
    '103.163.51.254:80',
    '209.97.150.167:8080',
    '117.54.114.102:80',
    '91.189.177.186:3128',
    '67.43.236.20:18277',
    '46.47.197.210:3128',
    '67.43.228.250:3057',
    '128.199.202.122:3128',
    '185.217.199.176:4444',
    '172.93.213.177:80',
    '91.189.177.188:3128',
    '72.10.164.178:4869',
    '72.10.164.178:22019',
    '116.203.28.43:80',
    '103.105.76.216:8080',
    '85.192.63.67:80',
    '49.13.137.5:80',
    '60.12.168.114:9002',
    '67.43.228.253:2431',
    '41.89.16.6:80',
    '104.129.199.51:10160',
    '103.36.136.138:8090',
    '93.171.220.229:8888',
    '104.129.206.209:8800',
    '182.34.18.191:38801',
    '114.231.8.117:8089',
    '165.225.72.156:10089',
    '104.129.192.167:8800',
    '117.250.3.58:8080',
    '178.46.163.102:3128',
    '154.65.39.7:80',
    '142.11.227.126:3128',
    '103.183.99.202:8080',
    '213.233.177.180:3000',
    '114.231.46.103:8888'
]

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#    'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'get_words.middlewares.GetWordsSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'get_words.middlewares.GetWordsDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'get_words.pipelines.NewGetWordsPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = 'utf-8'
