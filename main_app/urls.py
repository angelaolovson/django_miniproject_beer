from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"), # <- here we have added the new path
    path('about/', views.About.as_view(), name="about"),
    path('breweries/', views.BreweryList.as_view(), name="brewery_list"),
    path('beers/', views.BeerList.as_view(), name="beer_list"),
    path('breweries/new/', views.BreweryCreate.as_view(), name="brewery_create"),
    path('breweries/<int:pk>/', views.BreweryDetail.as_view(), name="brewery_detail"),
    path('breweries/<int:pk>/update',views.BreweryUpdate.as_view(), name="brewery_update"),
    path('breweries/<int:pk>/delete',views.BreweryDelete.as_view(), name="brewery_delete"),
]