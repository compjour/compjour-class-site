import requests
import shutil
import os.path
from glob import glob
from tempfile import NamedTemporaryFile

DATA_URL = 'http://stash.compjour.org/data/sunlight-twitter-opener.zip'
DATA_DIR = 'data-hold'
# Download the file

tzip = NamedTemporaryFile(suffix = '.zip')
print("Downloading", DATA_URL)
r = requests.get(DATA_URL)
tzip.write(r.content)
tzip.seek(0)
print("Unzipping to", DATA_DIR)
shutil.unpack_archive(tzip.name, DATA_DIR)
# close tzip (which automatically deletes it)
tzip.close()

csvname = os.path.join(DATA_DIR, 'sunlight_legislators.csv')
print(csvname, 'has', os.path.getsize(csvname), 'bytes')
print("There are", len(glob('data-hold/tweets/*.json')), 'json tweet files')
print("There are", len(glob('data-hold/profiles/*.json')), 'json profile files')
