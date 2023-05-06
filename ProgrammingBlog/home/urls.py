from django.urls import path
from . import views

urlpatterns= [
    # path('', views.index, name='home'), #1. parametre yol, 2. parametre yanıt, 3. parametre isim
    # path('<int:detailNumber>/', views.details, name='detail'),
    # path('<int:archiveNumber>/archive/', views.archive, name='archive'),
    # path('comment/<int:commentNumber>/', views.comment, name='comment')

    path('', views.index, name='index'),
    path('<int:riddle_id>/', views.detail, name='detail'), #home/1 home/2 ile sondaki sayı(id) deki riddle'ı görmemiz sağlandı
    path('check_answer/<int:riddle_id>/', views.check_answer, name='check_answer'), #<int:riddle_id> ile çakışmaması için başa check_answer eklendi
    path('search_results/', views.search_results, name='search_results'), #search result için path oluşturuldu
    #path('<int:riddle_id>/answer/', views.answer, name='answer'),

]