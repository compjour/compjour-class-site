import shutil
import requests
import re
from glob import glob
from os import makedirs
SITEURL = 'http://stash.compjour.org/data/ssa/%s.zip'
babyslugs = ['nationwide', 'state']

for slug in babyslugs:
    print("Downloading", SITEURL % slug)
    zdata = requests.get(SITEURL % slug).content
    makedirs(slug, exist_ok = True)
    with open(slug + '.zip', 'wb') as zf:
         zf.write(zdata)
         zf.seek(0)
         shutil.unpack_archive(zf.name, slug)



## Now combine the files
## state files:
with open("combined-state.csv", "w") as ofile:
    ofile.write('state,sex,year,name,count\n')
    for txtf in glob('state/*.TXT'):
       with open(txtf) as f:
            ofile.write(f.read())

## nationwide
with open("combined-nationwide.csv", "w") as ofile:
    ofile.write('name,sex,count,year\n')
    for txtf in glob('nationwide/*.txt'):
       with open(txtf) as f:
            year = re.search('\d{4}', txtf).group()
            for line in f.readlines():
                nline = line.strip() + ',' + year
                ofile.write(nline + "\n")

