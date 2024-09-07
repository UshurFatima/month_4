from django.urls import path
from . import views

urlpatterns = [
    path('post_list/', views.post_list_view),
    path('post_list/<int:id>/', views.post_detail_view),

    path('hello/', views.hello_view),
]