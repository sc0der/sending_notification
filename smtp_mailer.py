import smtplib


class Smtp(object):
    
    
    def __init__(self, to,  SUBJECT):
        self.to = to
        self.SUBJECT = SUBJECT   
        self.send_mail()   
        
    def send_mail(self):
        BODY = "\r\n".join((
            "From: %s" % "aliffortest@gmail.com",
            "To: %s" % self.to,
            "Subject: %s" % "self.SUBJECT" ,
            "",
        ))
        smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo()
        smtpserver.login('aliffortest@gmail.com', '$aliftestPwd$')
        smtpserver.sendmail("aliffortest@gmail.com", self.to, BODY)
        return "SUCCESS" 
            
            
