from django.db import models

# Create your models here.
class Brewery(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=1000)
    location = models.CharField(max_length=250)
    bio = models.TextField(max_length=500)
    verified_brewery = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Beer(models.Model):

    title = models.CharField(max_length=150)
    type = models.CharField(max_length=150)
    abv = models.IntegerField(default=0)
    brewery = models.ForeignKey(Brewery, on_delete=models.CASCADE, related_name="beers")

    def __str__(self):
        return self.title
    

class ShoppingCartlist(models.Model):

    title = models.CharField(max_length=150)
    # this is going to create the many to many relationship and join table
    beers = models.ManyToManyField(Beer)

    def __str__(self):
        return self.title