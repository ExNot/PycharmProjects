from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),  #/articles
    path('<str:title>/', views.article_detail, name='article_detail'), ##/articles/The Art and Importance of Riddles, #/articles/Unraveling the Mysteries of Riddles ....
]