from django.urls import path
from . import views  # アプリのviews.pyをインポート

urlpatterns = [
    path('', views.index, name='index'),  # トップページ
]