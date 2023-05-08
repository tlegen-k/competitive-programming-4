import datetime
import calendar
#Program determines the name of the day given the input of date in YYYY-MM-DD format

#input_date = input("Please entry the date to determine the day of the week in the YYYY-MM-DD format: ")

input_date = datetime.datetime.fromisoformat("2023-01-02")

#convert to the number in the week
day_number = input_date.weekday()
day_number_name = calendar.day_name[day_number]

print(day_number_name)
