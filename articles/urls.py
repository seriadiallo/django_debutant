from django.urls import path

from .views import index, malist, create, detail

app_name = 'articles'

urlpatterns = [
    path('', index, name='index'),
    path('form/', create, name='create'),
    path('list/', malist, name='list'),
    path('<int:id>/', detail, name='detail'),
]
