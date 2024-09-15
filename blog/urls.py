from django.urls import path
from . import views

urlpatterns = [
    path('post_list/', views.post_list_view, name='post_list'),
    path('post_list/<int:id>/', views.post_detail_view),

    path('post_list_delete/', views.post_list_delete_view, name='post_list_delete'),
    path('post_list/<int:id>/delete/', views.post_drop_view),
    path('post_list_edit/', views.post_list_edit_view, name='post_list_edit'),
    path('post_list/<int:id>/update/', views.update_post_view),
    path('create_post/', views.create_post_view, name='add_news'),

    path('hello/', views.hello_view),
]