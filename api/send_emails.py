import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json

def main(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            emails = data['emails']
            sender = os.environ['omrmmmdli736@gmail.com']
            password = os.environ['sojf oxwh hqdh wttq']
            subject = "Test Email"
            text = "Test mesaji"

            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = sender
            msg['To'] = ', '.join(emails)
            msg['Subject'] = subject
            msg.attach(MIMEText(text, 'plain'))

            # Connect to Gmail's SMTP server
            smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            smtp_server.login(sender, password)

            # Send the email
            smtp_server.sendmail(sender, emails, msg.as_string())
            smtp_server.quit()

            return {
                "statusCode": 200,
                "body": json.dumps({"message": "Emails sent successfully"})
            }
        except Exception as e:
            return {
                "statusCode": 500,
                "body": json.dumps({"error": str(e)})
            }
    else:
        return {
            "statusCode": 405,
            "body": json.dumps({"error": "Method not allowed"})
        }
