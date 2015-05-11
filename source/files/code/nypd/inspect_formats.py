"""

"""

import os.path
import re
from collections import Counter, defaultdict
from glob import glob
NYPD_RAW_PATH = 'data-hold/raw'

csvfiledict = {}
allheaders = []
csvfiles = glob(os.path.join(NYPD_RAW_PATH, '*.csv'))
for csvname in csvfiles:
    with open(csvname) as c:
        headers = c.readline().strip().split(',')
        csvfiledict[re.search('\d{4}', csvname).group()] = {'headers': headers, 'extra': [] }
        allheaders.extend(headers)

extraheaders = defaultdict(list)
allheaders = Counter(allheaders).most_common()
for col, ct in allheaders:
    if ct < len(csvfiles): # for non-ubiquitous headers
        for c, d in csvfiledict.items():
            if col in d['headers']:
                d['extra'].append(col)
                extraheaders[col].append(c)


import csv
# make csv
printdict = {}
for y, v in csvfiledict.items():
    printdict[y] = sorted(v['extra'])
