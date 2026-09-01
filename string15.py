numbers = [10, 45, 23, 67, 12]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest =", largest)