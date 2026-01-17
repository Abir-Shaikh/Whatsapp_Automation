from twilio.rest import Client
from datetime import datetime
import time
import os

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

client = Client(account_sid, auth_token)

def send_wp_msg(recipent_no, message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=message_body,
            to=f'whatsapp:{recipent_no}'
        )
        print(f"Message sent successfully! Message SID: {message.sid}")
    except Exception as e:
        print("An error occurred:", e)

name = input("Enter the recipient name: ")
recipent_number = input("Enter the recipient WhatsApp number with country code: ")
message_body = input(f"Enter the message you want to send to {name}: ")

date_str = input("Enter the date (YYYY-MM-DD): ")
time_str = input("Enter the time (HH:MM in 24 hr format): ")

schedule_datetime = datetime.strptime(
    f"{date_str} {time_str}", "%Y-%m-%d %H:%M"
)

delay_seconds = (schedule_datetime - datetime.now()).total_seconds()

if delay_seconds <= 0:
    print("The specified time is in the past.")
else:
    print(f"Message scheduled for {schedule_datetime}")
    time.sleep(delay_seconds)
    send_wp_msg(recipent_number, message_body)
