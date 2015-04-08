import csv
import os.path
DATA_DIR = 'data-hold'
csvname = os.path.join(DATA_DIR, 'sunlight_legislators.csv')
# not sure why we have to specify 'utf-8' encoding here. Oh well
csvdata = csv.DictReader(open(csvname, encoding = 'utf-8'))
# turn it into a list that we can easily traverse
congressmembers = []
for row in csvdata:
    congressmembers.append(row)
# Note: the Pythonic idiom is to do a list comprehension
# congressmembers = [row for row in csvdata]
print("There are {} Congressmembers listed".format(len(congressmembers)))

# filter for active congressmembers
# again, pythonic way is:
# active_members = [m for m in congressmembers if m['in_office'] == '1']
active_members = []
for m in congressmembers:
    if m['in_office'] == '1':
        active_members.append(m)
print("There are {} active Congressmembers".format(len(active_members)))

# Now we want active members who are in California
ca_active_members = []
for m in active_members:
    if m['state'] == 'CA':
        ca_active_members.append(m)
print("There are {} active Congressmembers from CA".format(len(ca_active_members)))

# Python list comprehensions can be confusing. The following snippet:
# ca_tweeters = []
# for m in ca_active_members:
#     if m['twitter_id'] != '':
#           ca_twitters.append(m)
ca_tweeters = [m for m in ca_active_members if m['twitter_id'] != '']
print("There are active CA Congressmembers from CA on Twitter".format(len(ca_tweeters)))
# yes, the list comprehension syntax can be hard to understand
