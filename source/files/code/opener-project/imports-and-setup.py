# the import statement is used to call in other files/libraries of code
import sys
print("I am using Python:", sys.version)

dirname = "data-hold/stuff"
print("I am making a new local directory named", dirname)

import os
# the `makedirs` function takes in options: in this case, the `exist_ok`
# option tells it not to throw an error if the directory exists
os.makedirs(dirname, exist_ok = True)
