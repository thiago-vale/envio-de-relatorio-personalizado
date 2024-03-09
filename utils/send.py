import smtplib
import email.message

class Send():

    def __init__(self):
        self.msg = email.message.Message()
        self.gmail = smtplib.SMTP('smtp.gmail.com: 587')


    
    def send_mail(self, msg, recipient, user, password, subject):

        """
        Sends an email containing a report.

        Parameters:
        msg (str): The report to be included in the email body.
        recipient (str): The email address of the recipient.
        user (str): The email address of the sender.
        password (str): The sender's password for SMTP authentication.
        subject (str): The subject of the email.

        Returns:
        None: This function doesn't return anything, but sends an email with the report to the recipient.

        User Script:
        

        Example:
        >>> send_mail("Restaurant Report...", "example@example.com", "youremail@gmail.com", "yourpassword", "Subject")
        Email sent
        """

        corpo_email = msg
        
        msg = email.message.Message()
        msg['subject'] = subject
        msg['from'] = user
        msg['To'] = recipient
        password = password
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(corpo_email)

        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()

        s.login(msg['From'], password)
        s.sendmail(msg['from'],msg['To'], msg.as_string().encode('utf-8'))
        print('Email enviado')