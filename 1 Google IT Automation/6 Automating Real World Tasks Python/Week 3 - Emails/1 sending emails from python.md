<style>hr{opacity: 20%; height: 1px!important; margin-bottom:0px!important</style>

## Email Library <hr/>
`SMTP` and `MIME` standards define how email messages are constructoed.  `email` is a built-in python module. 
```python
from email.message import EmailMessage

sender = "me@example.com"
recipient = "you@example.com"
body = """Hey there! \nI'm learning to send emails using Python!"""

message = EmailMessage()

# From, To, And Subject are Email Header Fields
# They're key-value pair of labels and instruction for routing and displaying the email
message['From'] = sender
message['To'] = recipient
message['Subject'] = 'Greetings from {} to {}!'.format(sender, recipient)

# Set Header automatically add couple of headers. 
# Content-Type and Content-Transfer-Encoding headers tell how to interpret the bytes into a string
message.set_content(body)

print(message) # Outputs in Human Readable Way
```

<br>

## Attachment <hr/>
Email are all made of strings. When you want to attach file, it has to be encoded to some form of text.

`MIME` use to encode all sorts of file as text string.<br>
You must attach MIME type and subtype.

Thhe Internet Assigned Numbers Authority `IANA`, hosts a registry of valid MIME types. If you know the correct type/subtype, you can use that directly.

`mimetypes` module take a good guess what file's MIME is
```python
import mimetypes
mime_type, _ = mimetypes.guess_type(attachment_path)
print(mime_type) # image/png
mime_type, mime_subtype = mime_type.split('/', 1)

# Add this attachment to the message var earlier
with open(attachment_path, 'rb') as ap:
     message.add_attachment(ap.read(),
                            maintype=mime_type,
                            subtype=mime_subtype,
                            filename=os.path.basename(attachment_path))
```

This is the Result. The whole message has MIME "multipart/mixed"

```json
Content-Type: multipart/mixed; boundary="===============5350123048127315795=="

--===============5350123048127315795==
Content-Type: text/plain; charset="utf-8"
Content-Transfer-Encoding: 7bit

Hey there!

I'm learning to send email using Python!

--===============5350123048127315795==
Content-Type: image/png
Content-Transfer-Encoding: base64
Content-Disposition: attachment; filename="example.png"
MIME-Version: 1.0

iVBORw0KGgoAAAANSUhEUgAAASIAAABSCAYAAADw69nDAAAACXBIWXMAAAsTAAALEwEAmpwYAAAg
AElEQVR4nO2dd3wUZf7HP8/M9k2nKIJA4BCUNJKgNJWIBUUgEggCiSgeVhA8jzv05Gc5z4KHiqin
eBZIIBDKIXggKIeCRCAhjQAqx4UiCARSt83uzDy/PzazTDZbwy4BnHde+9qZydNn97Pf5/uUIZRS
(...We deleted a bunch of lines here...)
wgAAAABJRU5ErkJggg==

--===============5350123048127315795==--
```


<br>

## Sending the Email through SMTP Server <hr/>
Computer use SMTP to send email. 

`smtplib` : Python module to send an email
```python
import smtplib
mail_server = smtplib.SMTP('localhost')
... ConnectionRefusedError: [Errno 61] Connection refused
```
This error happen because there are no local SMTP server configured

We can connect using SMTP server for personal email address, search the name of email service and SMTP connection setting.

When you do that, there are a couple of things that you'll probably need to do : Use transport layer and authenticate to the service using username and password. Like so :
- You can connect to a remote SMTP using `TLS` (Transport Layer Security). Earlier version are `SSL` (Secure Sockets Layer). It is interchangeable. 

In `smtplib`, there are  two classes to do that kind of connection :
- `SMTP` class : Direct SMTP connection
- `SMTP_SSL` class : SMTP connection over SSL/TLS

Like so
```python
mail_server = smtplib.SMTP_SSL('smtp.example.com')
mail_server.set_debuglevel(1) # Set this to see behind the scenes
```

### Inputing a password and Authenticating
```python
import getpass
mail_pass = getpass.getpass('Password? ') # mail_pass can still be printed

mail_server.login(sender, mail_pass) # Return tuple of SMTP status code. If fails, the module raise exception
```

### Sending the Message
```python
mail_server.send_message(message) # Rturns dict of recipients that werent able to receive the message
mail_server.quit() # Closing the connection
```
