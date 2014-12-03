import glob
import os
import subprocess

from django.core.management.base import LabelCommand, CommandError


DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../data'))
EVENT_MASK = '{0}*.EV?'
CMD = 'cwgame -f 0,1,3,4,6-11,18,26-44,46-83 -x 4-59 -y {0} {1} > games-{0}.csv'


class Command(LabelCommand):
    args = '<year year ...>'
    help = 'Processes Retrosheet data for the specified years into usable csv files'

    def handle_label(self, year, **options):
        os.chdir(DATA_DIR)
        mask = EVENT_MASK.format(year)
        if len(glob.glob(mask)) == 0:
            raise CommandError('No event files for {0}, use retro_dl first'.format(year))
        self.stdout.write('Processing events for {0}...'.format(year))
        returncode = subprocess.Popen(CMD.format(year, mask), shell=True).wait()
        if returncode != 0:
            raise CommandError('Event files for {0} has errors, make sure they are patched')
