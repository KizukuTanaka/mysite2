from django.urls import path
from . import views

urlpatterns = [
    path('', views.ToppageView.as_view(), name='toppage'),
    path('sisuutaisuu/', views.SisuutaisuuView.as_view(), name='sisuutaisuu'),
    path('notice/', views.NoticeView.as_view(), name='notice'),
]
