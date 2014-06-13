from django.conf.urls import patterns, include, url
from django.conf import settings
from api import views



WP_RANK_PREFIX = r'wp-rank/'
PERSON_PATH = r'(?P<dob>[^/]+)/(?P<sex>[^/]+)/(?P<country>[^/]+)/'


urlpatterns = [
    # /api/1.0/countries/
    url(r'countries/', views.country_list),

    # /api/1.0/population/
    url(r'population/(?P<year>[^/]+)/(?P<country>[^/]+)/(?P<age>[^/]+)/', views.population_data),
    url(r'population/(?P<year>\d+)/(?P<country>[^/]+)/', views.population_data),
    url(r'population/(?P<country>[^/]+)/(?P<age>\d+)/', views.population_data),

    # /api/1.0/wp-rank/
    url(r'wp-rank/' + PERSON_PATH + r'today/', views.world_population_rank_today),
    url(r'wp-rank/' + PERSON_PATH + r'on/(?P<date>[^/]+)/', views.world_population_rank_by_date),
    url(r'wp-rank/' + PERSON_PATH + r'aged/(?P<age>[^/]+)/', views.world_population_rank_by_age),
    url(r'wp-rank/' + PERSON_PATH + r'ago/(?P<offset>[^/]+)/', views.world_population_rank_in_past),
    url(r'wp-rank/' + PERSON_PATH + r'in/(?P<offset>[^/]+)/', views.world_population_rank_in_future),
    url(r'wp-rank/' + PERSON_PATH + r'ranked/(?P<rank>[^/]+)/', views.date_by_world_population_rank),

    # /api/1.0/life-expectancy/
    url(r'life-expectancy/remaining/(?P<sex>[^/]+)/(?P<country>[^/]+)/(?P<date>[^/]+)/(?P<age>[^/]+)/', views.remaining_life_expectancy),
    url(r'life-expectancy/total/(?P<sex>[^/]+)/(?P<country>[^/]+)/(?P<dob>[^/]+)/', views.total_life_expectancy),
]
