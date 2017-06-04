from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^scraper', views.scraper, name='scraper'),
    url(r'^last', views.last, name='last'),
]