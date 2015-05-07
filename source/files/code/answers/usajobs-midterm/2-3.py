import json
with open("data-hold/domestic-jobcount.json") as f:
    domestic_data = json.loads(f.read())
with open("data-hold/intl-jobcount.json") as f:
    intl_data = json.loads(f.read())

# using standard for loop
dcount = 0
for d in intl_data:
    dcount += d[1]
print("There are %s international jobs." % dcount)


# using list comprehension and sum
icount = sum([d[1] for d in domestic_data])
# note, you don't need to use a list comprehension...
# this would work too:
# icount = sum(d[1] for d in intl_data)
# ...but rather than learn about iterators right now, easier
# ...to just be consistent with list comprehensions

print("There are %s domestic jobs." % icount)


