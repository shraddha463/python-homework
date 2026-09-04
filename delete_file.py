

import os

file_name = "copy.txt"

if os.path.exists(file_name):
    os.remove(file_name)
    print("File deleted successfully.")
else:
    print("File does not exist.")