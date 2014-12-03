import glob
import os
import shutil
import subprocess
from tempfile import TemporaryFile
import urllib.error
import urllib.request
from zipfile import ZipFile

from django.core.management.base import LabelCommand, CommandError


DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../data'))
RETROSHEET_URL = 'http://www.retrosheet.org/events/{0}eve.zip'
PATCH_MASK = '*{0}*.patch'


class Command(LabelCommand):
    args = '<year year ...>'
    help = 'Downloads and patches Retrosheet data for the specified years'

    def handle_label(self, year, **options):
        self.stdout.write('Downloading events for {0}...'.format(year))
        url = RETROSHEET_URL.format(year)
        try:
            with urllib.request.urlopen(url) as response, TemporaryFile() as temp:
                self.stdout.write('Extracting events for {0}...'.format(year))
                shutil.copyfileobj(response, temp)
                ZipFile(temp).extractall(DATA_DIR)

            path = os.path.join(DATA_DIR, PATCH_MASK.format(year))
            for patch_file in glob.glob(path):
                cmd = 'patch -N -d {0} < {1}'.format(DATA_DIR, patch_file)
                subprocess.call(cmd, shell=True)
        except urllib.error.HTTPError:
            raise CommandError('Could not download {0} events, they might not exist'.format(year))
