from django.contrib import admin
from eats.models import Restaurant, Nerd


class RestaurantAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'distance',
        'nerd',
    )
    search_fields = ['name']
    list_filter = ['nerd']
    save_on_top = True


class NerdAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'title',
        'nerd_bio_url',
    )
    save_on_top = True


admin.site.register(Nerd, NerdAdmin)
admin.site.register(Restaurant, RestaurantAdmin)