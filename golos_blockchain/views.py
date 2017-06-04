from django.http import HttpResponse
import logging
from steemdata.helpers import timeit
from steemdata_mongo.src.mongostorage import MongoStorage, Settings
from steemdata_mongo.src.scraper import scrape_operations
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


def last(request):
    m = MongoStorage()
    settings = Settings(m)
    last_block = settings.last_block()
    return HttpResponse(last_block)


def scraper(request):
    m = MongoStorage()
    with timeit():
        scrape_operations(m)
    return HttpResponse('OK!')
