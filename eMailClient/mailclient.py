import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

os.chdir(r'D:\PycharmProjects\Vorlesung\EinfProg\eMailClient')

cred = tuple(open("password.txt","r"))

pwd = cred[0]
sender = cred[1]
reciever = cred[2]

message = MIMEMultipart()
message["From"] = sender
message["To"] = reciever
message["Subject"] = "Mail me up, before you go go"

body = "Here's a funny python joke"

message.attach(MIMEText(body, "plain"))

filename = "python.jpg"

with open(filename, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

encoders.encode_base64(part)

part.add_header("Content-Disposition", f"attachment; filename= {filename}")
message.attach(part)
text = message.as_string()

port = 465
smtp_server ="smtp.gmail.com"

try:
    server = smtplib.SMTP_SSL(smtp_server, port, context=ssl.create_default_context())
    server.login(sender, pwd)
    server.sendmail(sender, reciever, text)
except:
    print("Error: Sending Mail failed")

