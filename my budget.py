'''
request for your monthly salary
request for your name
request for the item
request for the amount of the item
'''
# import textwrap


class MyBudget:
    def __init__(self):
        self.listing = []

    def budget(self):
        self.value = {}
        self.name = input('Enter your name:')
        self.salary = int(input('Enter your salary for this month:'))
        self.details = ['item to purchase', 'amount_of_item']

        for request in self.details:
            self.value[request] = input(' enter the {}:'.format(request))
        self.listing.append(self.value)

    def checkout(self):
        if int((self.value['amount_of_item'])) > self.salary:
            print('You do not have enough cash')
        elif int((self.value['amount_of_item'])) <= self.salary:
            balance = self.salary - int((self.value['amount_of_item']))
            print('your balance is {}, you may continue adding the items'.format(balance))
        else:
            print('yo')


my_budget = MyBudget()
my_budget.budget()
my_budget.checkout()
