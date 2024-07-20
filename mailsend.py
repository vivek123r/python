from email.message import EmailMessage
import os.path
import mimetypes
import smtplib
import ssl

# Creating the EmailMessage object
message = EmailMessage()

# Setting the sender, recipient, and subject
sender = "vivek987gm@gmail.com"
recipient = "vivek987pm@gmail.com"
message['From'] = sender
message['To'] = recipient
message['Subject'] = f'Greetings from {sender} to {recipient}!'

# Setting the email body
body = """hi there!
This is a test message.
Hope this works!
Regards,
Vivek"""
message.set_content(body)

# Specifying the attachment
filename = "1.png"
attachment_path = os.path.join(os.getcwd(), filename)
attachment_filename = os.path.basename(attachment_path)
mime_type, _ = mimetypes.guess_type(attachment_path)
mime_type, mime_subtype = mime_type.split('/', 1)

# Adding the attachment to the email
with open(attachment_path, 'rb') as ap:
    message.add_attachment(ap.read(), maintype=mime_type, subtype=mime_subtype, filename=attachment_filename)

# Printing the headers and body only for inspection
print(f"From: {message['From']}")
print(f"To: {message['To']}")
print(f"Subject: {message['Subject']}")
print(f"Body: {message.get_body(preferencelist=('plain')).get_content()}")

smtp_server = "smtp.gmail.com"
smtp_port = 465  # For SSL
smtp_username = sender  # Use the sender's email
smtp_password = "PM@VIV987"

# Create a secure SSL context
context = ssl.create_default_context()

# Send the email
try:
    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
        server.login(smtp_username, smtp_password)
        server.send_message(message)
    print("Email sent successfully!")
except Exception as e:
    print(f"Error sending email: {e}")
