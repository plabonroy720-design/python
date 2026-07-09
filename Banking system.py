def deposite(balance, amount):
    return balance+amount

def withdraw(balance, amount):
    if amount>balance:
        return "Insufficient Balance"
    else:
        return balance-amount
    
def check_balance(balance):
    return balance

balance=int(input("Enter your balance : "))

while True:

    print("")
    print("======== Bank System ========")
    print("")
    print('1 Deposite')
    print('2 Withdraw')
    print('3 Check Balance')
    print('4 Exit')
    print("")
 
    try:
        choice=int(input("Enter your choice : "))
        if choice==1:
            amount=int(input("How much you want to deposite : "))
            if amount>0:
                balance=deposite(balance,amount)
                print(balance)
            else:
                print("VALUE ERROR")

        elif choice==2:
            amount=int(input("How much you want to withdraw : "))
            balance=withdraw(balance, amount)
            print(balance)

        elif choice==3:
            balance=check_balance(balance)
            print(balance)

        elif choice==4:
            print("We are about to leave the system.......")
            print("THANK YOU FOR THE DAY.....")
            break

    except ValueError:
        print("Invalid Value....")
    finally:
        print("Successful")
