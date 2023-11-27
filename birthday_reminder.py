import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime


# cnydgmiiedpseuib
def send_email_reminder(receiver, subject, body):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "your_email@domain.com"
    contrasena = "Write Your Password Here"

    mensaje = MIMEMultipart()
    mensaje["From"] = sender_email
    mensaje["To"] = receiver
    mensaje["Subject"] = subject
    mensaje.attach(MIMEText(body, "plain"))

    with smtplib.SMTP(smtp_server, smtp_port) as smtp_server:
        smtp_server.starttls()
        smtp_server.login(sender_email, contrasena)
        smtp_server.sendmail(sender_email, receiver, mensaje.as_string())


def verify_birthday():
    today = datetime.date.today()

    # write the correct birthday for your case
    friend_birthday = datetime.date(today.year, 11, 25)

    remainder_days = (friend_birthday - today).days

    # send reminder if the birthday is in less than one week
    if 0 < remainder_days < 7:
        receiver = "receiver_email@domain.com"
        subject = "Birthday Reminder"
        body = f"Hello!\n\n¡Your friend's birthday is in {remainder_days} days!\n\n¡Don't forget it!"

        send_email_reminder(receiver, subject, body)
        print("Reminder succesfully sent!")


verify_birthday()
