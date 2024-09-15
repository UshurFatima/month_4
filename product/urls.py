from django.urls import path
from . import views

urlpatterns = [
    path('eat_food/', views.eat_list_view),
]