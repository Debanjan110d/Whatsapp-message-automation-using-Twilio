from twilio.rest import Client
    """
    The Python script schedules a WhatsApp message to be sent at a specified date and time using the
    Twilio API.
    
    :param phone_number: The `phone_number` parameter is the recipient's phone number in international
    format, including the country code. For example, if the phone number is in the United States, it
    should be in the format +1XXXXXXXXXX
    :param message_body: The `message_body` parameter in the code represents the content of the message
    that will be sent to the specified phone number via WhatsApp. This is the actual text that you want
    to send as a message. You can customize this message to include any information or instructions you
    want to communicate to the recipient
    """
import time 
from datetime import datetime, timedelta
from credentials import account_sid, auth_token

client = Client(account_sid, auth_token)

def send_message(phone_number, message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=message_body,
            to=f'whatsapp:+{phone_number}'
        )
        print(f"Message sent to {phone_number}: {message.sid}")
    except Exception as e:
        error_message = f"Error sending message to {phone_number}: {str(e)}"
        print(error_message)

name = input("Enter your name: ")
phone_number = input("Enter your phone number: ")
message_body = input(f"Enter your message to send to {phone_number}: ")

# Clear instructions for the correct format
date_input = input("Enter the date (YYYY-MM-DD, e.g., 2025-04-25): ")
time_input = input("Enter the time (HH:MM, e.g., 23:01): ")

try:
    schedule_datetime = datetime.strptime(f"{date_input} {time_input}", "%Y-%m-%d %H:%M")
except ValueError as ve:
    print(f"Error parsing date and time: {ve}")
    exit(1)

current_datetime = datetime.now()
time_difference = schedule_datetime - current_datetime
delay_seconds = time_difference.total_seconds()

if delay_seconds <= 0:
    print("The scheduled time has already passed. Please try again.")
else:
    print(f"Message will be sent to {phone_number} in {delay_seconds} seconds.")
    time.sleep(delay_seconds)
    send_message(phone_number, message_body)
