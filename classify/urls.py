from django.urls import path
from . import views

urlpatterns = [
    path('process_url/', views.process_url, name='process_url'),
    path('register/', views.register, name='register'),
    path('whitelist/', views.WhitelistView.as_view(), name='whitelist'),  # 화이트리스트 뷰 추가
]
