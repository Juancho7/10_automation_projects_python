from email.message import EmailMessage
from ssl import create_default_context
from smtplib import SMTP_SSL

email_sender = "user_sender@domain.com"
email_password = "Write Your Password Here"
email_receiver = "user_receiver@domain.com"

subject = "Automatic Email Sending App"
body = """
We are learning a lot! Continue studying!
"""

email = EmailMessage()
email["From"] = email_sender
email["to"] = email_receiver
email["Subject"] = subject
email.set_content(body)

context = create_default_context()


with SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, email.as_string())
