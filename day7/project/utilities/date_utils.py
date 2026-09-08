from datetime import date, datetime


def current_date():
    return date.today()


def current_time():
    return datetime.now().time()


def calculate_age(birth_year):
    current_year = date.today().year
    return current_year - birth_year


def days_between_dates(date1, date2):
    d1 = datetime.strptime(date1, "%Y-%m-%d")
    d2 = datetime.strptime(date2, "%Y-%m-%d")

    return abs((d2 - d1).days)