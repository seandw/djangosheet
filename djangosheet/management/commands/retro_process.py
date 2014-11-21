import glob
import os
import subprocess

from django.core.management.base import BaseCommand, CommandError


DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../data'))
EVENT_MASK = '{0}*.EV?'
CMD = 'cwgame -f 0,1,3,4,6-11,18,26-44,46-83 -x 4-59 -y {0} {1} > games-{0}.csv'


class Command(BaseCommand):
    args = '<year year ...>'
    help = 'Processes Retrosheet data for the specified years into usable csv files'

    def handle(self, *args, **options):
        os.chdir(DATA_DIR)
        for year in args:
            mask = EVENT_MASK.format(year)
            if len(glob.glob(mask)) == 0:
                self.stderr.write('No event files for {0}, use retro_dl first'.format(year))
                continue
            self.stdout.write('Processing events for {0}...'.format(year))
            returncode = subprocess.Popen(CMD.format(year, mask), shell=True).wait()
            if returncode != 0:
                raise CommandError('Event files for {0} has errors, make sure they are patched')