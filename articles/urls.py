from django.urls import path

from .views import index, malist, create

app_name = 'articles'

urlpatterns = [
    path('', index, name='index'),
    path('form/', create, name='create'),
    path('list/', malist, name='list'),
]
