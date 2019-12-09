# dev_mail
Simple Email Classes for Python Developers

Dev Mail provides 4 classes that simplify email operations for a developer needing
to implement mail messaging within their application. 

Simple

Provides simple text email message.
Example Usage: 

from mail import Simple

if __name__ == '__main__':
message = Simple(
	'sender email address',
	'sender password',
	'recipient email address',
	'subject',
	'body',
)
message.send()

The calls for the other 3 classes are almost identical. For the Attachment and Fancy classes,attachments must be passed as a list.

Each subsequent class is a child class of Simple(), and only extends its functionality.

Enjoy!
