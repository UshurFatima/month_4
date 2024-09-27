from django.urls import path
from . import views

urlpatterns = (
    path('manas_films/', views.ManasFilmListView.as_view(), name='manas_film_list'),
    path('start_parsing/', views.ParserFormView.as_view()),
)