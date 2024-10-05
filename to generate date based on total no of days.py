'''Function that generates a string which has entire date with the date,month and year based on the total no of days given
by the user as input'''

import datetime
day_number=int(input("enter the total no of days:"))
year=int(input("enter the year :"))
def day_to_date(day_number, year):
    start_date = datetime.datetime(year, 1, 1)
    final_date = start_date + datetime.timedelta(days=day_number - 1)
    formatted_date = final_date.strftime("%d %B, %Y")
    
    return formatted_date
print(day_to_date(day_number,year))

