from twilio.rest import Client

class Sms(object):
    def __init__(self, message, phone):
        self.message = message
        self.phone = phone
    
    @property
    def send_sms(self):
        account_sid = 'AC413c8c702a2ccd07c149ec21fc8312de'
        auth_token = '8900633aa3ab7610215d94c4fb67a1e4'
        client = Client(account_sid, auth_token)
        MESSAGE = client.messages\
                .create(
                     body=self.message,
                     from_='+16105699914',
                     to=self.phone
                 )
        if MESSAGE.sid["status"] == "sent":
            return "SUCCESS"
        else:
            return "FAIL"