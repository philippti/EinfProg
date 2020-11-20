# This small script will set up a secured SSL connection to a mail server and attach a file to it.
# The passwort, sender mail and reciever mail address are stored in a text file and read by opening it
# and storing it as a tuple.
# Make sure the working directory is set correctly, to access the textfile and the file you want to send
# with the email 
# 
# author: philippti
# created: 20.11.2020

import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

#set the working directory so python knows where the textfile and attatchment are stored
os.chdir(r'PATH TO YOUR WORKING DIRECTORY')

# open credential file with passwort, sender and reciever mail address from a file
# store as tuple to access lines individualy
cred = tuple(open("infos.txt","r"))

pwd = cred[0]
sender = cred[1]
reciever = cred[2]

# create MIME Header to send
message = MIMEMultipart()
message["From"] = sender
message["To"] = reciever
message["Subject"] = "Mail me up, before you go go"

# body of the Mail, the text you want to write in the mail
body = "Here's a funny python joke"

# attatching the body to the MIME message as plain text
message.attach(MIMEText(body, "plain"))

# defining the file you want to attatch to the mail
filename = "python.jpg"

# open file "filename" (here a jpg) in read mode as a binary file ("rb")
with open(filename, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")  # set to application/octet-stream, since attatchment is sent as binary
    part.set_payload(attachment.read())             # read in the attachment and add as payload to the part

# encode to ASCII 
encoders.encode_base64(part)    

# add part top the message, set header
part.add_header("Content-Disposition", f"attachment; filename= {filename}")
message.attach(part)
text = message.as_string()

port = 465                      # set port for smtp
smtp_server ="smtp.gmail.com"   # smtp gmail server

# try to send the email using secured SSL connection, if it fails, print error message, and finally close the connection to the server
try:
    server = smtplib.SMTP_SSL(smtp_server, port, context=ssl.create_default_context())
    server.login(sender, pwd)
    server.sendmail(sender, reciever, text)
except:
    print("Error: Sending Mail failed")
finally:
    server.close()

