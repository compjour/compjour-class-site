import requests
import shutil
import os.path
from glob import glob
from tempfile import NamedTemporaryFile

DATA_URL = 'http://stash.compjour.org/data/sunlight-twitter-opener.zip'
DATA_DIR = 'data-hold'

# This NamedTemporaryFile class is just a better convention
# for handling a file (in this case, a zip file) that I know I don't want
# to keep around
tzip = NamedTemporaryFile(suffix = '.zip')
# Download the file
print("Downloading", DATA_URL)
r = requests.get(DATA_URL)
tzip.write(r.content)
# Think of a file object as a cassette tape
# after writing data to it, we want to rewind (or "seek" the 0 position)
tzip.seek(0)
print("Unzipping to", DATA_DIR)
shutil.unpack_archive(tzip.name, DATA_DIR)
# close tzip (which automatically deletes it)
tzip.close()

csvname = os.path.join(DATA_DIR, 'sunlight_legislators.csv')
print(csvname, 'has', os.path.getsize(csvname), 'bytes')
print("Tweet files:", len(glob('data-hold/tweets/*.json')))
print("Profile files:", len(glob('data-hold/profiles/*.json')))
