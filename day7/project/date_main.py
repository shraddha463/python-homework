from date_utils import current_date, current_time, calculate_age, days_between_dates

print("Current Date:", current_date())
print("Current Time:", current_time())

birth_year = int(input("Enter your birth year: "))
print("Age:", calculate_age(birth_year))

date1 = input("Enter first date (YYYY-MM-DD): ")
date2 = input("Enter second date (YYYY-MM-DD): ")

print("Days between dates:", days_between_dates(date1, date2))
