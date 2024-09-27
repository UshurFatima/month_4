from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('post_list/<int:id>/', views.PostDetailView.as_view()),
    path('search/', views.SearchView.as_view(), name='search'),

    path('post_list_delete/', views.PostListDeleteView.as_view(), name='post_list_delete'),
    path('post_list/<int:id>/delete/', views.PostDropDeleteView.as_view()),
    path('post_list_edit/', views.PostUpdateListView.as_view(), name='post_list_edit'),
    path('post_list/<int:id>/update/', views.PostEditView.as_view()),
    path('create_post/', views.PostCreateView.as_view(), name='add_news'),

    path('hello/', views.hello_view),
]