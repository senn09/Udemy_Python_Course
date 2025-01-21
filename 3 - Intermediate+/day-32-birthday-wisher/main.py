import smtplib
import random
import datetime as dt

with open("quotes.txt", 'r') as file:
    quotes = file.readlines()

quote_of_the_day = random.choice(quotes)

weekday = ""
if dt.datetime.now().weekday() == 0:
    weekday = "Monday"
elif dt.datetime.now().weekday() == 1:
    weekday = "Tuesday"
elif dt.datetime.now().weekday() == 2:
    weekday = "Wednesday"
elif dt.datetime.now().weekday() == 3:
    weekday = "Thursday"
elif dt.datetime.now().weekday() == 4:
    weekday = "Friday"
elif dt.datetime.now().weekday() == 5:
    weekday = "Saturday"
elif dt.datetime.now().weekday() == 6:
    weekday = "Sunday"


my_email = ""
password = ""

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email,to_addrs="",
                        msg=f"Subject:{weekday} quote of the day\n\n{quote_of_the_day}")



