import requests
import shutil
import os.path
from glob import glob
from tempfile import NamedTemporaryFile

DATA_URL = 'http://stash.compjour.org/data/sunlight-twitter-opener.zip'
DATA_DIR = 'data-hold'

# Download the file
print("Downloading", DATA_URL)
r = requests.get(DATA_URL)
# This NamedTemporaryFile class is just a better convention
# for handling a file (in this case, a zip file) that I know I don't want
# to keep around
# Note: Revision to this script
# Apparently NamedTemporaryFile is borked on Windows
# https://bugs.python.org/issue14243

# The following code will work fine, though.
tzip = NamedTemporaryFile(delete = False)
tzip.write(r.content)
tzip.close()
print("Unzipping to", DATA_DIR)
shutil.unpack_archive(tzip.name, DATA_DIR, format = 'zip')
os.remove(tzip.name) # again, thanks a lot Windows
csvname = os.path.join(DATA_DIR, 'sunlight_legislators.csv')
print(csvname, 'has', os.path.getsize(csvname), 'bytes')
print("Tweet files:", len(glob('data-hold/tweets/*.json')))
print("Profile files:", len(glob('data-hold/profiles/*.json')))
