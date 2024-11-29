from django.db import models

from django.db import models
import requests
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
    def get_videos(self):
        url = f"https://api.themoviedb.org/3/movie/{self.id}/videos?language=en-US"
        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0ODVlMTBmYTA2MWIwNTFhOTQ2ODBhZGIzMDYwMmNiZSIsIm5iZiI6MTczMjg4NzU1My4zNTQ0OTU1LCJzdWIiOiI2NzFhYjAxMTViZTllODc1OWRhNzBlOTEiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.94dfNSwJHOrEgLCQuDgnQfbR2Zy496PE6BqQpRxkpsc"
        }
        response = requests.get(url, headers=headers)
        data = response.json()
        trailers = [video for video in data['results'] if video['type'] == 'Trailer']
        video_url=[]
        images=[]
        for trailer in trailers:
            video_url.append(f"https://www.youtube.com/watch?v={trailer['key']}")
            images.append(f"https://img.youtube.com/vi/{ trailer['key'] }/0.jpg")
        return video_url,images
    def __str__(self):
        return self.title
    # djosnfsdbf