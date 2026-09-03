def calculate_total(marks):
    return sum(marks)

def calculate_percentage(marks):
    total = sum(marks)
    return (total / (len(marks) * 100)) * 100

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 75:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 40:
        return "C"
    else:
        return "Fail"
