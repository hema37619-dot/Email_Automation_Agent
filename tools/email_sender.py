import smtplib

from email.mime.text import MIMEText

from config.settings import (
    EMAIL_ADDRESS,
    EMAIL_PASSWORD
)

def send_email(
    receiver,
    subject,
    body
):

    msg = MIMEText(body)

    msg["From"] = EMAIL_ADDRESS
    msg["To"] = receiver
    msg["Subject"] = subject

    server = smtplib.SMTP(
        "smtp.gmail.com",
        587
    )

    server.starttls()

    server.login(
        EMAIL_ADDRESS,
        EMAIL_PASSWORD
    )

    server.send_message(msg)

    server.quit()