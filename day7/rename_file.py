import os
old_name="old file.txt"
new_name="new file.txt"
with open (old_name,"w") as file:
    file.write("hello python")
os.rename(old_name,new_name)
print("file renamed successfully.")    