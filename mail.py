#!/usr/bin/env python
import email, smtplib, ssl
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

class Simple():
        
        def __init__(self, sender, recipient, password, subject, text):
                
                self.sender = sender
                self.password = password
                self.recipient = recipient
                self.subject = subject
                self.text = text
                
        def send_mail(self):

                message = 'Subject: {}\n\n{}'.format(self.subject, self.text)

                server_connect = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server_connect.ehlo()
                server_connect.login(self.sender, self.password)
                server_connect.sendmail(self.sender, self.recipient, message) 
                
class Html_Message(Simple):
        
        def __init__(self, sender, recipient, password, subject, text, html):
                
                Simple.__init__(self, sender, recipient, password, subject, text)
                self.html = html
                
        def send_mail(self):
                
                SMTP_INFO = {
                        'host': 'smtp.gmail.com',
                        'port': 587,
                        'username': self.sender,
                        'password': self.password
                }
                
                SENDER_NAME = 'SYSTEM'
                RECIPIENT = self.recipient
                SUBJECT = self.subject
                BODY_PLAIN_TEXT = self.text
                BODY_HTML = self.html
                
                message = MIMEMultipart('alternative')
                message['From'] = f"{SENDER_NAME} <{SMTP_INFO['username']}>"
                message['To'] = RECIPIENT
                message['Subject'] = SUBJECT
                
                #Adding the plain text email body
                message.attach(MIMEText(BODY_PLAIN_TEXT, 'plain'))
                
                #Adding the HTML email BODY_HTML
                message.attach(MIMEText(BODY_HTML, 'html'))
                
                #SMTP server connection
                with smtplib.SMTP(SMTP_INFO['host'], SMTP_INFO['port']) as smtp:
                        
                        #encrypt the connection
                        smtp.starttls()
                        
                        #Logging in and sending the email:
                        smtp.login(SMTP_INFO['username'], SMTP_INFO['password'])
                        smtp.send_message(message)

class Attachment(Simple):

        def __init__(self, sender, recipient, password, subject, text, attachments):
                
                # Attachments are passed as a list
                Simple.__init__(self, sender, recipient, password, subject, text)
                self.attachments = attachments
        
        def send_mail(self):

                SMTP_INFO = {
                        'host': 'smtp.gmail.com',
                        'port': 587,
                        'username': self.sender,
                        'password': self.password
                }
                
                SENDER_NAME = 'SYSTEM'
                RECIPIENT = self.recipient
                SUBJECT = self.subject
                BODY_PLAIN_TEXT = self.text
                FILES = self.attachments

                message = MIMEMultipart('alternative')
                message['From'] = f"{SENDER_NAME} <{SMTP_INFO['username']}>"
                message['To'] = RECIPIENT
                message['Subject'] = SUBJECT

                #Adding the plain text email body
                message.attach(MIMEText(BODY_PLAIN_TEXT, 'plain'))

                # Add the attachment
                # Open files in binary mode
                for f in FILES:
                        with open(f, "rb") as attached_file:
                                # Add file as application/octet-stream
                                # Email client can usually download this automatically as attachment
                                part = MIMEBase("application", "octet-stream")
                                part.set_payload(attached_file.read())
                        
                        # Encode file in ASCII characters to send by email
                        encoders.encode_base64(part)
                        part.add_header(
                                "Content-Disposition",
                                f"attachment; filename={f}",
                        )
                
                        # Add attachment to message and convert message to string
                        message.attach(part)

                #SMTP server connection
                with smtplib.SMTP(SMTP_INFO['host'], SMTP_INFO['port']) as smtp:
                        
                        #encrypt the connection
                        smtp.starttls()
                        
                        #Logging in and sending the email:
                        smtp.login(SMTP_INFO['username'], SMTP_INFO['password'])
                        smtp.send_message(message)

class Fancy(Simple):

        def __init__(self, sender, recipient, password, subject, text, attachments, html):
                
                # Attachments are passed as a list
                Simple.__init__(self, sender, recipient, password, subject, text)
                self.attachments = attachments
                self.html = html
        
        def send_mail(self):

                SMTP_INFO = {
                        'host': 'smtp.gmail.com',
                        'port': 587,
                        'username': self.sender,
                        'password': self.password
                }
                
                SENDER_NAME = 'SYSTEM'
                RECIPIENT = self.recipient
                SUBJECT = self.subject
                BODY_PLAIN_TEXT = self.text
                BODY_HTML = self.html
                FILES = self.attachments

                message = MIMEMultipart('alternative')
                message['From'] = f"{SENDER_NAME} <{SMTP_INFO['username']}>"
                message['To'] = RECIPIENT
                message['Subject'] = SUBJECT

                #Adding the plain text email body
                message.attach(MIMEText(BODY_PLAIN_TEXT, 'plain'))

                # Add the attachment
                # Open files in binary mode
                for f in FILES:
                        with open(f, "rb") as attached_file:
                                # Add file as application/octet-stream
                                # Email client can usually download this automatically as attachment
                                part = MIMEBase("application", "octet-stream")
                                part.set_payload(attached_file.read())
                        
                        # Encode file in ASCII characters to send by email
                        encoders.encode_base64(part)
                        part.add_header(
                                "Content-Disposition",
                                f"attachment; filename={f}",
                        )
                
                        # Add attachment to message and convert message to string
                        message.attach(part)
                
                #Adding the HTML email BODY_HTML
                message.attach(MIMEText(BODY_HTML, 'html'))

                #SMTP server connection
                with smtplib.SMTP(SMTP_INFO['host'], SMTP_INFO['port']) as smtp:
                        
                        #encrypt the connection
                        smtp.starttls()
                        
                        #Logging in and sending the email:
                        smtp.login(SMTP_INFO['username'], SMTP_INFO['password'])
                        smtp.send_message(message)