from django.urls import path
from .views import (
    index, news_list,
    news_detail, add_news, edit_news,
    delete_news, members_list,
    members_details, add_members,
    edit_members, delete_members,
    about_us, our_works, law,
)

urlpatterns = [
    path('', index, name='index'),
    path('about_us', about_us, name='about_us'),
    path('our_works', our_works, name='our_works'),
    path('international_law',law, name='international_law'),
    path('news/', news_list, name='news_list'),
    path('news/<int:pk>/', news_detail, name='news_detail'),
    path('add_news/', add_news, name='add_news'),
    path('edit/<int:pk>/', edit_news, name='edit_news'),
    path('delete/<int:pk>/', delete_news, name='delete_news'),
    path('members/', members_list, name='members_list'),
    path('members/<int:pk>/', members_details, name='members_details'),
    path('add_members/', add_members, name='add_members'),
    path('edit_members/<int:pk>/', edit_members, name='edit_members'),
    path('delete_members/<int:pk>/', delete_members, name='delete_members')
]
