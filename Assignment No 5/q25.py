class ATM:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def show_balance(self):
        print(self.__balance)

a = ATM(5000)
a.deposit(1500)
a.withdraw(900)
a.show_balance()