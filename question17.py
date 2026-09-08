bill = float(input("Enter total bill amount: "))

if bill > 1000:
    discount = bill * 20 / 100
elif bill >= 500:
    discount = bill * 10 / 100
else:
    discount = 0

final_amount = bill - discount

print("Discount =", discount)
print("Final Amount =", final_amount)