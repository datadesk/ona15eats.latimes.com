from django.db import models


class Restaurant(models.Model):
    """
    A place to eat
    """
    name = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    distance = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    restaurant_url = models.CharField(max_length=200, blank=True)
    photo_url = models.CharField(max_length=200, blank=True)
    photo_credit = models.CharField(max_length=200, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)
    address = models.CharField(max_length=1000, blank=True)
    nerd = models.ForeignKey("Nerd", blank=True, null=True)
    CATEGORY_CHOICES = (
        ('eats', 'Eats'),
        ('bars', 'bars'),
        ('extras', 'Extracurricular'),
    )
    category = models.CharField(
        max_length=200,
        choices=CATEGORY_CHOICES,
        default='eats'
    )

    class Meta:
        ordering = ("distance",)


class Nerd(models.Model):
    """
    A smart person recommending a place to eat
    """
    name = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=200, blank=True)
    image_url = models.CharField(max_length=200, blank=True)
    nerd_bio_url = models.CharField(max_length=200, blank=True)

    
