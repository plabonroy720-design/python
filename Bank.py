class Bank:
    def __init__(self, balance):
        self.__balance=balance
    
    def show__balance(self):
        print(f'Current Balance : {self.__balance}')
    def deposite(self, amount):
        self.__balance+=amount
        print("")
        print(f'Deposite : {amount}')
        print("")
        print(f'Current Balance : {self.__balance}')
    def withdraw(self, withdraw):
        self.__balance-=withdraw
        print("")
        print(f'Withdraw : {withdraw}')
        print(f'Current Balance : {self.__balance}')
a=Bank(int(input("Enter the amount : ")))
a.show__balance()
a.deposite(int(input("Enter the amount you want to deposite : ")))
a.withdraw(int(input("Enter the amount you want to withdraw : ")))
