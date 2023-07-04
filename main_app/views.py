from django.shortcuts import redirect
from .models import Brewery, Beer, ShoppingCartlist
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.views import View


# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["shoppingcartlists"] = ShoppingCartlist.objects.all()
        return context

    

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

class BreweryDetail(DetailView):
    model = Brewery
    template_name = "brewery_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["shoppingcartlists"] = ShoppingCartlist.objects.all()
        return context


class BreweryCreate(CreateView):
    model = Brewery
    fields = ['name', 'img','location', 'bio', 'verified_brewery']
    template_name = "brewery_create.html"
    success_url = "/breweries/"

class BreweryUpdate(UpdateView):
    model = Brewery
    fields = ['name', 'img', 'location', 'bio', 'verified_brewery']
    template_name = "brewery_update.html"
    success_url = "/breweries/"

class BreweryDelete(DeleteView):
    model = Brewery
    template_name = "brewery_delete_confirmation.html"
    success_url = "/breweries/"

class BeerList(TemplateView):
    template_name = "beer_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["beers"] = Beer.objects.all() # this is where we add the key into our context object for the view to use
        return context

class BeerCreate(View):
    def post(self, request, pk):
        title = request.POST.get("title")
        type = request.POST.get("type")
        abv = request.POST.get("abv")
        brewery = Brewery.objects.get(pk=pk)
        Beer.objects.create(title=title,type=type ,abv=abv, brewery=brewery)
        return redirect('brewery_detail', pk=pk)
    
class ShoppingCartlistBeerAssoc(View):
    def get(self, request, pk, beer_pk):
        # get the query param from the url
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            # get the playlist by the id and
            # remove from the join table the given song_id
            ShoppingCartlist.objects.get(pk=pk).beers.remove(beer_pk)
        if assoc == "add":
            # get the ShoppingCartlist by the id and
            # add to the join table the given song_id
            ShoppingCartlist.objects.get(pk=pk).beers.add(beer_pk)
        return redirect('home')
