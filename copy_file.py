source = open("messages.txt", "r")

content = source.read()

source.close()

destination = open("copy.txt", "w")

destination.write(content)

destination.close()

print("File copied successfully.")
