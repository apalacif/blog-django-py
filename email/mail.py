#!/usr/bin/env python

# import necessary packages

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# create message object instance
msg = MIMEMultipart()


message = "Thank you"

# setup the parameters of the message
password = "df59pu32"
msg['From'] = "apalacif@educacion.navarra.es"
msg['To'] = "apalacif@gmail.com"
msg['Subject'] = "Subscription"

# add in the message body
msg.attach(MIMEText(message, 'plain'))

#create server
server = smtplib.SMTP('176.12.82.3: 25')

#server.starttls()

# Login Credentials for sending the mail
server.login(msg['From'], password)


# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())

server.quit()

