file = open("messages.txt", "r")

content = file.read(5)

print("First 5 characters:", content)

file.close()