import json
with open("data-hold/intl-jobcount.json") as f:
    intl_list = json.loads(f.read())

def myfoo(x):
    return x[1]

for d in sorted(intl_list, key = myfoo, reverse = True):
    if d[1] > 10:
        print("%s,%s" % (d[0], d[1]))
