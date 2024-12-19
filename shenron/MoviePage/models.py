from django.db import models

from django.db import models
import requests
from datetime import datetime
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
    
    def get_movie_data_by_title(self, title):
        url = f"https://api.themoviedb.org/3/search/movie?query={title}&language=en-US"
        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0ODVlMTBmYTA2MWIwNTFhOTQ2ODBhZGIzMDYwMmNiZSIsIm5iZiI6MTczMjg4NzU1My4zNTQ0OTU1LCJzdWIiOiI2NzFhYjAxMTViZTllODc1OWRhNzBlOTEiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.94dfNSwJHOrEgLCQuDgnQfbR2Zy496PE6BqQpRxkpsc"
        }

        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()

            if 'results' in data and len(data['results']) > 0:
                for movie_data in data['results']:
                    if movie_data['title'].strip().lower() == title.strip().lower():
                        movie_id = movie_data['id']
                        
                        movie_details_url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
                        new_response = requests.get(movie_details_url, headers=headers)
                        
                        if new_response.status_code == 200:
                            movie_details_data = new_response.json()
                            print(movie_details_data)
                            movie_details = {
                                'id': movie_details_data['id'],
                                'title': movie_details_data['title'],
                                'vote_average': movie_details_data['vote_average'],
                                'vote_count': movie_details_data['vote_count'],
                                'status': movie_details_data.get('status', 'Unknown'),
                                'release_date': datetime.strptime(movie_details_data['release_date'], '%Y-%m-%d').date() if movie_details_data.get('release_date') else None,
                                'revenue': movie_details_data['revenue'],
                                'runtime': movie_details_data['runtime'],
                                'adult': movie_details_data['adult'],
                                'backdrop_path': movie_details_data.get('backdrop_path', ''),
                                'budget': movie_details_data['budget'],
                                'original_language': movie_details_data['original_language'],
                                'overview': movie_details_data['overview'],
                                'poster_path': movie_details_data.get('poster_path', ''),
                                'tagline': movie_details_data.get('tagline', ''),
                                'genres': ', '.join([genre['name'] for genre in movie_details_data['genres']]),
                                'keywords': ', '.join([keyword['name'] for keyword in movie_details_data.get('keywords', {}).get('results', [])])
                            }
                            return movie_details
                        else:
                            return None
                return None
            else:
                return None
        else:
            return None


    def __str__(self):
        return self.title

