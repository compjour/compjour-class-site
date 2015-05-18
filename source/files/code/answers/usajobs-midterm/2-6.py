import json
from operator import itemgetter
with open("data-hold/intl-jobcount.json") as f:
    data = json.loads(f.read())

sorted_data = sorted(data, key = itemgetter(1), reverse = True)
for d in sorted_data[0:10]:
    print("%s,%s" % (d[0], d[1]))


others = sum([d[1] for d in sorted_data[10:-1]])
print("Others,%s" % others)
