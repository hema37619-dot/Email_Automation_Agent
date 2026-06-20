import smtplib

EMAIL = "yourmail@gmail.com"
APP_PASSWORD = "abcdefghijklmnop"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(EMAIL, APP_PASSWORD)

print("Login Successful")

server.quit()