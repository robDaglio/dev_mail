#!/usr/bin/env python
from mail_attachment import Fancy

if __name__ == '__main__':

    sender = "sender email address"
    recipient = "recipient email address"
    password = "sender account password"
    subject = "email subject"
    text = "email text body"
    attachments = ['test.txt', 'test_2.txt']

    html_message = """<!DOCTYPE html>
        <html lang='en'>
            <html>
                <head>
                    <style type='text/css'>
                        p{
                            color:red;
                        }
                    </style>
                </head>
                <body>
                    <p>This is just a test</p>
                </body>
            </html>
    """
    
    new_message = Fancy(
        sender, 
        recipient, 
        password, 
        subject, 
        text, 
        attachments, 
        html_message
    )
    
    new_message.send_mail()
    print("[*] Sent!")