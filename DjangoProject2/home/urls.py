from django.urls import path
from . import views

# url = uniform resource locator

urlpatterns = [
    path("", views.index, name='home'),
    path("<int:detailNumber>/", views.details, name='details'), #path("details/", views.details, name='details')
    path('<int:archiveNumber>/archive/', views.archive, name='archive'),    #detailNumber ile archiveNumber'ı ayırt etmek için sonuna /archive/ ekledik
    path('comment/<int:commentNumber>/', views.comment, name='comment')
]
