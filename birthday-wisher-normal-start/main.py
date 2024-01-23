##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import datetime as dt
import random
import pandas

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
# birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

today = dt.datetime.now()
today_tuple = (today.month,today.day)

my_email = "steveudemy09@gmail.com"
password = "jrwhslmfypsqqfnw"

birthday_letter = ""
print(birthdays_dict)
if today_tuple in birthdays_dict:
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as letter_file:
        birthday_letter += letter_file.read().replace('[NAME]', birthdays_dict[today_tuple]["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="steveudemy09@yahoo.com",
                            msg=f"Subject:Happy Birthday\n\n{birthday_letter}")
