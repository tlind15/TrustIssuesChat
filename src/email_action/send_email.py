import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


class SendEmail(object):

    @staticmethod
    def send_email(recipient_email, rsa_public_key_path):
        sender_email, email_password, smtp = SendEmail._get_email_info()

        subject = 'RSA'
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = recipient_email

        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(rsa_public_key_path, "rb").read())
        encoders.encode_base64(part)

        part.add_header('Content-Disposition', 'attachment; filename="public.pem"')

        msg.attach(part)

        # 'smtp.ionos.com'
        server = smtplib.SMTP_SSL(smtp, 465)
        server.ehlo()
        server.login(sender_email, email_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()

    @staticmethod
    def _get_email_info():
        print("\nPlease ensure that your email provider allows SMTP")
        sender = input("\nEnter your email address: ")
        password = input("Enter your email password: ")
        smtp = input("Enter the SMTP server url for your email_action provider: ")
        return sender, password, smtp
