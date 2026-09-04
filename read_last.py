file = open("messages.txt", "r")

content = file.read()

last_10 = content[-10:]

print("Last 10 characters:", last_10)

file.close()