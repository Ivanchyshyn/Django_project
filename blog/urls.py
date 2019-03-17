from django.urls import path
from .views import article_view, article_list_view, create_article_view

app_name='blog'
urlpatterns = [
    path('', article_list_view, name="article-list"),
    path('article/<int:id>/', article_view, name="article"),
    path('create-article/', create_article_view, name="create-article"),
]