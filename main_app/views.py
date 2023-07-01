from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Brewery
from django.views.generic.edit import CreateView


# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
    template_name = "home.html"
    

class About(TemplateView):
    template_name = "about.html"

class BreweryList(TemplateView):
    template_name = "brewery_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["breweries"] = Brewery.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["breweries"] = Brewery.objects.all() # this is where we add the key into our context object for the view to use
            context["header"] = "All Breweries"
        return context

class BreweryCreate(CreateView):
    model = Brewery
    fields = ['name', 'img','location', 'bio', 'verified_brewery']
    template_name = "brewery_create.html"
    success_url = "/breweries/"


class BeerList(TemplateView):
    template_name = "beer_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["beers"] = beers # this is where we add the key into our context object for the view to use
        return context

class Beer:
    def __init__(self, title, type, abv):
        self.title = title
        self.type = type
        self.abv = abv

beers =[
    Beer('AMBIO','Sour DIPA w/ wheat & oat, milk sugar, raspberry, lychee, toasted coconut & rose petals','8%'),
    Beer('AMBIENT FIZZ','Spritzy Spontaneous Sour','4%')
]