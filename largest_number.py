file = open("numbers.txt", "r")

numbers = []

for line in file:
    number = int(line)
    numbers.append(number)

file.close()

largest = max(numbers)

print("Largest number:", largest)