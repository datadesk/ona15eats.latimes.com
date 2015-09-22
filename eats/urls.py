from eats import views
from django.conf import settings
from django.conf.urls import patterns, include, url


urlpatterns = patterns('', 
    url(r'^$', views.RestaurantListView.as_view(), name='restaurants'),
)
