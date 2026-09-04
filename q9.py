def percentage(marks):
    total = sum(marks)
    percentage = total / len(marks)
    return percentage


marks = [80, 75, 90, 85, 70]

print("Student Percentage =", percentage(marks), "%")