import os
from twilio.rest import Client

# Using a .env file to retrieve the phone numbers and tokens.

class NotificationManager:

    def __init__(self):
        self.client = Client(os.environ['ACCOUNT_SID'], os.environ["AUTH_TOKEN"])

    def send_sms(self, message_body):

        message = self.client.messages.create(
            from_=os.environ["TWILIO_VIRTUAL_NUMBER"],
            body=message_body,
            to=os.environ["MY_NUMBER"]
        )
        # Prints if successfully sent.
        print(message.sid)