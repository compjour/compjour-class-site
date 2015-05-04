import shutil
import requests
SITEURL = 'http://stash.compjour.org/data/ssa/combined-%s.zip'
babyslugs = ['nationwide', 'state']
for slug in babyslugs:
    print("Downloading", SITEURL % slug)
    zdata = requests.get(SITEURL % slug).content
    with open(slug + '.zip', 'wb') as zf:
         zf.write(zdata)
         zf.seek(0)
         shutil.unpack_archive(zf.name)

