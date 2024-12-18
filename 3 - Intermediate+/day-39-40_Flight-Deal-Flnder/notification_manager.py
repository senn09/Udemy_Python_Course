import os
from twilio.rest import Client
import smtplib

# Using a .env file to retrieve the phone numbers and tokens.

class NotificationManager:

    def __init__(self):
        self.client = Client(os.environ['ACCOUNT_SID'], os.environ["AUTH_TOKEN"])
        self.smtp_email = os.environ['SMTP_EMAIL']
        self.password = os.environ['PASSWORD']

    def send_sms(self, message_body):

        message = self.client.messages.create(
            from_=os.environ["TWILIO_VIRTUAL_NUMBER"],
            body=message_body,
            to=os.environ["MY_NUMBER"]
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, email_list, email_body):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.smtp_email, password=self.password)
            for email in email_list:
                connection.sendmail(from_addr=self.smtp_email, to_addrs=email,
                                    msg=f"Subject:New Flight Deal\n\n{email_body}")
