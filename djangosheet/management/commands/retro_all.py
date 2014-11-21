from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    args = '<year year ...>'
    help = 'Runs retro_{dl, process, load} for each provided year'

    def handle(self, *args, **options):
        call_command('retro_dl', *args)
        call_command('retro_process', *args)
        call_command('retro_load', *args)