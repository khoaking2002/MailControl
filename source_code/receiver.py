import email
import imaplib

EMAIL = 'thaovo2962002@gmail.com'
PASSWORD = 'a2k46pbc'


class Receiver:
    def __init__(self,username, password):
        self.SERVER = 'imap.gmail.com'
        self.username = username
        self.password = password
    def get_mail(self):
        self.mail =  imaplib.IMAP4_SSL(self.SERVER)
        self.mail.login(self.username,self.password)
        self.mail.select('inbox')
        status, data = self.mail.search(None,'ALL')
        mail_ids = data[-1].split()
        i =  mail_ids[-1]
        status, data = self.mail.fetch(i, '(RFC822)')
        for response_part in data:
            # so if its a tuple...
            if isinstance(response_part, tuple):
                message = email.message_from_bytes(response_part[1])
                mail_from = message['from']
                mail_subject = message['subject']
                date_mail = message["Date"]
                if message.is_multipart():
                    mail_content = ''
                    for part in message.get_payload():
                        if part.get_content_type() == 'text/plain':
                            mail_content += part.get_payload()
                else:
                    # if the message isn't multipart, just extract it
                    mail_content = message.get_payload()

                # and then let's show its result
                # print(f'From: {mail_from}')
                # print(f'Subject: {mail_subject}')
                # print(f'Content: {mail_content}')
        return mail_subject,mail_content,date_mail
    