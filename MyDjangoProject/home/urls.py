from django.urls import path
from . import views

#unifrom_resource_locator = url

urlpatterns = [
    path("", views.index, name='home'),
    #path('<int: detailNumber>/', views.detail, name='detail'),
    path('<int:archiveNumber>/archive/', views.archive,name='archive')

]

#'<int: detailNumber>/' yerinde 'detail' vardı