from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"), # <- here we have added the new path
    path('about/', views.About.as_view(), name="about"),
    path('breweries/', views.BreweryList.as_view(), name="brewery_list"),
    path('beers/', views.BeerList.as_view(), name="beer_list"),
]