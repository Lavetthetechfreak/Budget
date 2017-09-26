class Contact:
    def __init__(self):

        self.values = {}

    def get_contact(self):
        name = input('Enter name:')
        email = input('Enter email:')

        self.values[name] = email
        print(self.values)

mest_party = Contact()
mest_party.get_contact()




