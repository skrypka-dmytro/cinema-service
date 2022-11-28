from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError
import time


class Command(BaseCommand):
    """Django command to pause execution until database is available"""

    def handle(self, *args, **kwargs):
        """Handle the command"""
        self.stdout.write("waiting for db ...")
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections["default"]
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second ...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
