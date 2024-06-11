# Code adapted from
# https://www.programiz.com/python-programming/datatime/current-datatime

from datetime import date

# get today's date
today = date.today()

# Get day, month and year as individual strings
day = today.strftime("%D")
month = today.strftime("%M")
year = today.strftime("%Y")

heading = "The current date is {}/{}/{]".format(day, month, year)
filename = "MMF_{}_{}{}".format(year, month, day)

# Heading
print(heading)
print("The filename wil be {}.txt". format(filename))

