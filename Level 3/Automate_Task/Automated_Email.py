import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd
from datetime import datetime, timedelta

def send_reminder_email(to_email, name, smtp_server, port, from_email, password):
    subject = "Subscription Renewal Reminder"
    body = (f"Dear {name},\n\n"
            "We wanted to remind you that your subscription is about to end. "
            "To continue enjoying uninterrupted service, please renew your subscription at your earliest convenience.\n\n"
            "Thank you for your attention.\n"
            "Best regards,\n"
            "Magic Moves Inc.")

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()
            server.login(from_email, password)
            server.sendmail(from_email, to_email, msg.as_string())
            print(f"Reminder sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")

def automate_reminders(csv_file, smtp_server, port, from_email, password):
    df = pd.read_csv(csv_file)

    today = datetime.now().date()

    for _, row in df.iterrows():
        email = row['email']
        name = row['name']
        end_date = pd.to_datetime(row['subscription_end_date']).date()

        if end_date - today <= timedelta(days=7):
            send_reminder_email(email, name, smtp_server, port, from_email, password)


csv_file = input("Enter the path to the CSV file with recipient details(format: email,name,subscription_end_date): ")
smtp_server = "smtp.gmail.com"
port = 587
from_email = input("Enter your Gmail address: ")
password = input("Enter your Gmail app password: ")

automate_reminders(csv_file, smtp_server, port, from_email, password)
