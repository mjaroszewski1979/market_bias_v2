import smtplib
import imghdr
from email.message import EmailMessage
from os import environ

email_address = 'mjaroherokuapp@gmail.com'
email_password = 'mjaroherkuapp1234'


def send_mail(email):
    message = "Your free ebook from Market Bias"
    msg = EmailMessage()
    msg['Subject'] = 'Free Ebook'
    msg['From'] = 'Market Bias'
    msg['To'] = email
    msg.set_content(message)  

    with open('MarketBiasEbook.pdf', 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)  

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)