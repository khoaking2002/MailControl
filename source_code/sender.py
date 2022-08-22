import sys
from smtplib import SMTP_SSL as SMTP      
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import os
class Sender:
    def __init__(self,uname,passw):
        self.SMTP_Host = 'smtp.gmail.com'
        self.sender = uname
        self.passw = passw
        self.conn = SMTP(self.SMTP_Host)
        self.conn.set_debuglevel(False)
        self.conn.login(self.sender, self.passw)
    def send(self,content,subject,receivers):
        try:
            text_subtype = 'plain'
            msg = MIMEText(content, text_subtype)
            msg['Subject'] = subject
            msg['From'] = self.sender  
            try:
                self.conn.sendmail(self.sender, receivers, msg.as_string())
                print("Send success")
            finally:
                print("Ending")
        except Exception as error:
            print("Some thing wrong")
            print(error)
    def image_send(self,content,ImgFileName,subject,receivers):
        with open(ImgFileName, 'rb') as f:
            img_data = f.read()

        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = self.sender 
        text = MIMEText(content)
        msg.attach(text)
        image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
        msg.attach(image)
        self.conn.sendmail(self.sender,receivers, msg.as_string())
    def destroy(self):
        self.conn.quit()
#--------------

