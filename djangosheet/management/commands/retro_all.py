from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    args = '<year year ...>'
    help = 'Runs retro_{dl, process, load} for each provided year'

    def handle(self, *args, **options):
        errors = dict()
        for year in args:
            try:
                call_command('retro_dl', year)
                call_command('retro_process', year)
                call_command('retro_load', year)
            except CommandError as error:
                self.stderr.write(error.__str__())
                errors[year] = error
        if len(errors) > 0:
            errors_str = '\n'.join('{0}: {1}'.format(year, error) for year, error in errors.items())
            raise CommandError('The following years couldn\'t be processed:\n' + errors_str)
