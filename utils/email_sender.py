import smtplib
from email.mime.text import MIMEText

def send_email(config, recipient_email, subject, body):
    try:
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = config["sender_email"]
        msg["To"] = recipient_email

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(config["sender_email"], config["app_password"])
            server.sendmail(config["sender_email"], recipient_email, msg.as_string())

        print(f"Email sent to {recipient_email}")
        return True

    except Exception as e:
        print(f"Failed to send to {recipient_email}: {e}")
        return False
