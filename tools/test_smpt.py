import smtplib

EMAIL = "yourgmail@gmail.com"
PASSWORD = "your_app_password"

server = smtplib.SMTP(
    "smtp.gmail.com",
    587
)

server.starttls()

server.login(
    EMAIL,
    PASSWORD
)

print("Login Successful")

server.quit()