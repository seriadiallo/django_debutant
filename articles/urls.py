from django.urls import path

from .views import ArticleDeleteView, index, malist, create, detail

app_name = 'articles'

urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('list/', malist, name='list'),
    path('<int:id>/', detail, name='detail'),
    path('<int:id>/delete', ArticleDeleteView.as_view(), name='delete'),
    
]
