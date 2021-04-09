#!/usr/bin/env python

# import necessary packages

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# create message object instance
msg = MIMEMultipart()


message = "Build realizado"

# setup the parameters of the message
password = ""
msg['From'] = "apalacif@educacion.navarra.es"
msg['To'] = "apalacif@gmail.com"
msg['Subject'] = "Build blog"

# add in the message body
msg.attach(MIMEText(message, 'plain'))

#create server
server = smtplib.SMTP('176.12.82.3: 25')

#server.starttls()

# Login Credentials for sending the mail (no es necesario)
#server.login(msg['From'], password)


# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())

server.quit()

