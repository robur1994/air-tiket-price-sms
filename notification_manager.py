import os

from twilio.rest import Client


TWILLIO_SID = os.environ['TWILLIO_SID']
TWILLIO_TOKEN = os.environ['TWILLIO_TOKEN']
PHONE_NUM = os.environ['PHONE_NUM']
VERIFY_NUM = os.environ['VERIFY_NUM']


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILLIO_SID, TWILLIO_TOKEN)


    def send_notification(self, messages):
        messages = self.client.messages.create(body=messages,
                                               from_=PHONE_NUM,
                                               to=VERIFY_NUM,)
        print(messages.sid)
