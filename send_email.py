import smtplib
from email.message import EmailMessage

def send_hotmail_email(sender_email, sender_password, recipient_email, subject, message):
    try:
        # Create an EmailMessage object
        email = EmailMessage()
        email["From"] = sender_email
        email["To"] = recipient_email
        email["Subject"] = subject
        email.set_content(message)

        # Connect to Hotmail"s SMTP server
        smtp_server = "smtp-mail.outlook.com"
        smtp_port = 587
        smtp = smtplib.SMTP(smtp_server, smtp_port)
        smtp.starttls()

        # Login to your Hotmail account
        smtp.login(sender_email, sender_password)

        # Send the email
        smtp.send_message(email)

        # Close the SMTP server
        smtp.quit()

        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
