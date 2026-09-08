file = open("numbers.txt", "r")

even = 0
odd = 0

for line in file:
    number = int(line)

    if number % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

file.close()

print("Even numbers:", even)
print("Odd numbers:", odd)