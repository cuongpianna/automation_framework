import smtplib
from email.message import EmailMessage


# msg = EmailMessage()
#
#
# msg['Subject'] = 'The contents of %s'
# msg['From'] = 'cuongpianna1996@gmail.com'
# msg['To'] = 'cuongpianna1996@gmail.com'
#
# s = smtplib.SMTP('smtp.gmail.com', 587)
# s.ehlo()
# s.starttls()
# s.ehlo()
# s.login("cuongpianna1996@gmail.com", "01649886076")
# s.send_message(msg)
# s.quit()


def send_email(from_email, to_email, subject, body):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email
    msg.set_content(body)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("cuongpianna1996@gmail.com", "01649886076")
    server.send_message(msg)
    server.quit()
