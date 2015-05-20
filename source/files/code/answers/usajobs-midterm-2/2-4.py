import json
with open("data-hold/domestic-jobcount.json") as f:
    domestic_list = json.loads(f.read())

for v in sorted(domestic_list):
    if v[1] < 100:
        print("%s,%s" % (v[0], v[1]))
