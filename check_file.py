import os

file_name = "messages.txt"

if os.path.exists(file_name):
    print("File exists.")
else:
    print("File does not exist.")