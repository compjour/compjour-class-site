import os.path

filenames = [
"hello-world.py",
"imports-and-setup.py",
"stanford-news-download.py",
"stanford-news-heds.py",
"stanford-news-topics.py",
"get-er-done.py",
"fetch-and-unpack-twitter-data.py",
"read-sunlight-csv.py",
"read-twitter-json.py",
"twitter_foo.py",
"twitter_foo_fun.py",
"twitter-tablemaker.py",
"twitter-word-tweets.py"
]


# check to see if directory is named properly
current_path = os.path.dirname(os.path.realpath(__file__))
if current_path.split('/')[-1] != 'opener-project':
    print("Warning: the project directory needs to be named: opener-project")

# check to see if each file exists and if it's at least 100 bytes or bigger
missing_files = []
for fn in filenames:
    if os.path.exists(fn) == False or os.path.getsize(fn) < 100:
        missing_files.append(fn)
        print(fn, "...Unfinished")
    else:
        print(fn, "...Finished!")


# if there are missing files, print out a report
if len(missing_files) > 0:
    print("###################")
    print("{} missing files".format(len(missing_files)))
    for fn in missing_files:
        print(fn)
else:
    print("""
    All done (theoretically...)!
    You should now be able to turn in the assignment by pushing it to Github
    """)
