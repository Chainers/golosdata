from django.core.management.base import BaseCommand, CommandError
from steemdata_mongo.src.mongostorage import MongoStorage, Settings
from steemdata_mongo.src.scraper import scrape_operations
from steemdata.helpers import timeit


class Command(BaseCommand):
    help = 'run scraper blockchain'

    def add_arguments(self, parser):
        parser.add_argument('start', nargs='+', type=str)

    def handle(self, *args, **options):
        if len(options['start']) > 1:
            end_block = int(options['start'][1])
            m = MongoStorage()
            with timeit():
                scrape_operations(m, end_block)
        else:
            m = MongoStorage()
            with timeit():
                scrape_operations(m)
