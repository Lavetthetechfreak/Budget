class Account:
    '''
    create a simple bank account that you can withdraw and check balance
    '''

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print('Thank you' + self.name)

    def deposit(self, amount):
        if self.balance > 0:
            self.balance += amount
            print(self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(self.balance)
        else:
            print('Withdraw cash that is less or equal to the money in your bank account')

    def check_balance(self):
        print('your balance is {}'.format(self.balance))


account = Account('Lavet', 1000)
account.deposit(500)
account.withdraw(400)
account.check_balance()
