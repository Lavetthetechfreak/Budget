import smtplib
from email.mime.text import MIMEText
from smtplib import SMTPException

class Event:
    def __init__(self):

        self.all_contacts = []
        self.value = {}

    def contact(self):
        self.contacted = ['name', 'email']
        for request in self.contacted:
            self.value[request] = input('Enter your {}:'.format(request))
        self.all_contacts.append(self.value)
        print(self.all_contacts)

    def get_email(self):
        single_email = self.all_contacts

        self.my_name = input('Enter a name to get the email:')

        for values in single_email:
            if self.my_name == values['name']:
                print(values['email'])
                break

    def send_email(self):
        sender = 'lavet@gmail.com'
        receiver = 'ubuntuclass18@gmail.com '
        message = """From: From Person <from@fromdomain.com>
        To: To Person <ubuntuclass18@gmail.com >
        Subject: SMTP e-mail test

        This is a test e-mail message.
        """
        try:
            smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
            smtpobj.starttls()
            smtpobj.login(" ubuntuclass18@gmail.com ", "codewizard")
            smtpobj.sendmail(sender, receiver, message)
            print("Successfully sent email")
        except SMTPException:
            print("Error: unable to send email")






    def main(self):
        while True:
            print('Choose A or Q')
            self.request = input('''
                A.Enter your contact details
                B.get emails
                C.Send email
                Q.Quit
            ''')
            if self.request == 'A':
                self.contact()
            elif self.request == 'B':
                self.get_email()
            elif self.request == 'C':
                self.send_email()
            elif self.request == 'Q':
                break

            else:
                print('Sorry')


event = Event()
event.main()
event.send_email()





