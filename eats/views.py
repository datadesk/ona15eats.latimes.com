from django.shortcuts import render
from eats.models import Restaurant, Nerd
from bakery.views import BuildableDetailView, BuildableListView


class RestaurantListView(BuildableListView):
    """
    A buildable list of restaurants folks should eat at
    """
    queryset = Restaurant.objects.all()
