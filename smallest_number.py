file = open("numbers.txt", "r")

numbers = []

for line in file:
    number = int(line)
    numbers.append(number)

file.close()

smallest = min(numbers)

print("Smallest number:", smallest)