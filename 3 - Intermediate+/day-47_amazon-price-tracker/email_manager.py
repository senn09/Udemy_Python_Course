import smtplib
import os
from dotenv import load_dotenv

# Load the .env file into the environment
load_dotenv()

class Email_Manager:
    def __init__(self):
        self.smtp_email = os.getenv("SMTP_EMAIL")
        self.smtp_password = os.getenv("SMTP_PASSWORD")
        self.recipient_email = os.getenv("RECIPIENT_EMAIL")

    def send_email(self, item, price, link):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.smtp_email, password=self.smtp_password)
            connection.sendmail(from_addr=self.smtp_email, to_addrs=self.recipient_email,
                                msg=f"Subject:Price Alert for {item}\n\n{item} is now {price}\n{link}".encode("utf-8"))