def validate_name(name):
    return name.strip() != ""


def validate_roll_no(roll_no):
    return roll_no.strip() != ""


def validate_marks(marks):
    for mark in marks:
        if mark < 0 or mark > 100:
            return False

    return True
