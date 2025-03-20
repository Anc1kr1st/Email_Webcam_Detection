import smtplib
from PIL import Image
import io
from email.message import EmailMessage

PASSWORD = "password"
SENDER = "example@gmail.com"
RECEIVER = "example@gmail.com"


def send_email(image_path):
    print("send_email function start")
    email_message = EmailMessage()
    email_message["Subject"] = "New customer showed up!"
    email_message.set_content("Hey, we just saw a new customer!")

    with open(image_path, "rb") as file:
        content = file.read()
    try:
        with Image.open(io.BytesIO(content)) as img:
            subtype = img.format.lower()
    except IOError:
        subtype = None

    email_message.add_attachment(content, maintype="image", subtype=subtype)

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()
    print("send_email function start")

if __name__ == "__main__":
    send_email(image_path="images/30.png")