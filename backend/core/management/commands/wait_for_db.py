import time

from django.core.management import BaseCommand
from django.db import OperationalError
from django.db import connection as con
from django.db.backends.base.base import BaseDatabaseWrapper

connection: BaseDatabaseWrapper = con


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Wait for db...')
        db_con = False
        while not db_con:
            try:
                connection.ensure_connection()
                db_con = True
            except OperationalError:
                self.stdout.write('Database unavailable, wait 1 second...')
                time.sleep(1)
        self.stdout.write('Database available!!!')
