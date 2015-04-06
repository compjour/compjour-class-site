import sys
print("I am using Python:", sys.version)

dirname = "stuff"
print("I am making a new local directory named", dirname)

import os
# the `makedirs` function takes in options: in this case, the `exist_ok`
# option tells it not to throw an error if the directory exists
os.makedirs('stuff', exist_ok = True)



# http://stackoverflow.com/questions/847850/cross-platform-way-of-getting-temp-directory-in-python
# import tempfile
# print("The temporary directory on my computer is:", tempfile.gettempdir())
