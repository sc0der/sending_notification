from twilio.rest import Client

class Sms(object):
    def __init__(self, message, phone):
        self.message = message
        self.phone = phone
        account_sid = 'AC413c8c702a2ccd07c149ec21fc8312de'
        auth_token = '7341b36696ea1377ad81a8f69ca8f83e'
        client = Client(account_sid, auth_token)
        MESSAGE = client.messages \
                .create(
                     body=self.message,
                     from_='+16105699914',
                     to=self.phone
                 )
        print(MESSAGE)
        return "SUCCESS"