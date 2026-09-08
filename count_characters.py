file = open("messages.txt", "r")

content = file.read()

characters = len(content)

print("Number of characters:", characters)

file.close()