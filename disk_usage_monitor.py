from email.mime.text import MIMEText
from smtplib import SMTP
from psutil import disk_usage

email_sender = "user_sender@domain.com"
email_password = "Write Your Password Here"
email_receiver = "user_receiver@domain.com"
threshold_percent = 60


def send_email_alert(message):
    subject = "Disk Usage Alert"
    body = f"Avaliable disk space is under {threshold_percent}%. {message}"

    email_message = MIMEText(body)
    email_message["From"] = email_sender
    email_message["To"] = email_receiver
    email_message["Subject"] = subject

    with SMTP("smtp.gmail.com", 587) as servidor_smtp:
        servidor_smtp.starttls()
        servidor_smtp.login(email_sender, email_password)
        servidor_smtp.sendmail(email_sender, email_receiver, email_message.as_string())


# Write the path of the disk you want to track it's usage rate, for example C disk
disk_space = disk_usage("C:\\")
disk_space_percent = disk_space.percent

if disk_space_percent > threshold_percent:
    alert_message = f"Warning! The disk space used is {disk_space_percent}%."
    send_email_alert(alert_message)
else:
    print("The disk space usage is good.")
