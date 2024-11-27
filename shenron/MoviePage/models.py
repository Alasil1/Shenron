from django.db import models

from django.db import models

class Movie(models.Model):
    id = models.BigIntegerField(primary_key=True,null=False,blank=False)
    title = models.CharField(max_length=255,null=False,blank=False)
    vote_average = models.FloatField(null=False,blank=False)
    vote_count = models.IntegerField(null=False,blank=False)
    status = models.CharField(max_length=50,null=False,blank=False)
    release_date = models.DateField(null=False,blank=False)
    revenue = models.BigIntegerField(null=False,blank=False)
    runtime = models.IntegerField(null=False,blank=False)
    adult = models.BooleanField(null=False,blank=False)
    backdrop_path = models.CharField(max_length=255,null=False,blank=False)
    budget = models.BigIntegerField(null=False,blank=False)
    original_language = models.CharField(max_length=10,null=False,blank=False)
    overview = models.TextField(null=False,blank=False)
    poster_path = models.CharField(max_length=255,null=False,blank=False)
    tagline = models.CharField(max_length=255,null=False,blank=False)
    genres = models.CharField(max_length=255,null=False,blank=False)
    keywords = models.CharField(max_length=255,null=False,blank=False)

    # production_companies = models.ForeignKey(max_length=255)
    # production_countries = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    # djosnfsdbf