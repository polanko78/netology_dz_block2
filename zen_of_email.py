import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailClient:

    def __init__(self):
        self.gmail_smtp = "smtp.gmail.com"
        self.gmail_imap = "imap.gmail.com"
        self.login = 'login@gmail.com'
        self.password = 'qwerty'

    def send(self, **kwargs):
        # send message
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(kwargs['recipients'])
        msg['Subject'] = kwargs['subject']
        msg.attach(MIMEText(kwargs['message']))
        ms = smtplib.SMTP(self.gmail_smtp, 587)
        # identify ourselves to smtp gmail client
        ms.ehlo()
        # secure our email with tls encryption
        ms.starttls()
        # re-identify ourselves as an encrypted connection
        ms.ehlo()
        ms.login(self.login, self.password)
        ms.sendmail(self.login, ms, msg.as_string())
        ms.quit()
        # send end

    def recieve(self, header):
        # recieve
        mail = imaplib.IMAP4_SSL(self.gmail_imap)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()
        # end recieve


if __name__ == '__main__':
    my_client = EmailClient
    my_client.send(subject='Subject', message='Message', recipients=['vasya@email.com', 'petya@email.com'])
    my_client.recieve(header=None)
