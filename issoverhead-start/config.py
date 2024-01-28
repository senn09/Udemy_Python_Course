import smtplib

class Config():
    def __init__(self):

        self.my_email = "steveudemy09@gmail.com"
        self.password = "jrwhslmfypsqqfnw"

    def send_email(self):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.my_email,password=self.password)
            connection.sendmail(from_addr=self.my_email,to_addrs="steveudemy09@yahoo.com",
                                msg=f"Subject:ISS is overhead\n\nLook Up")