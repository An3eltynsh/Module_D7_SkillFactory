from django.urls import path
from .views import (
    NewsList, NewDetail, NewsSearch, CreateNews,
    CreatePost, NewsUpdate, PostUpdate, NewsDelete,
    PostDelete
)

urlpatterns = [
    path('', NewsList.as_view(), name='list'),
    path('<int:pk>', NewDetail.as_view(), name='new'),
    path('search/', NewsSearch.as_view()),
    path('create/', CreateNews.as_view(), name='news_create'),
    path('post/create/', CreatePost.as_view(), name='post_create'),
    path('<int:pk>/update/', NewsUpdate.as_view(), name='news_update'),
    path('post/<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('post/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    ]
