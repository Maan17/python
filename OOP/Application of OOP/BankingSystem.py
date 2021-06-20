from abc import ABCMeta, abstractmethod
import random

class Account(metaclass = ABCMeta):
    @abstractmethod
    def createAccount():
        return 0
    @abstractmethod
    def validate():
        return 0
    @abstractmethod
    def withdraw():
        return 0
    @abstractmethod
    def deposit():
        return 0
    @abstractmethod
    def checkBalance():
        return 0


class SavingsAccount:
    def __init__(self):
        self.savingsAccount = {}
        
    def createAccount(self, name, initialDeposit):
        self.accountNumber = random.randint(10000, 99999)
        self.savingsAccount[self.accountNumber] = [name, initialDeposit]
        print("Account Creation has been successful. Your Account Number is ", self.accountNumber)
        
    def validate(self, name, accountNumber):
        if accountNumber in self.savingsAccount.keys():
            if self.savingsAccount[accountNumber][0] == name:
                print("Authentication Successful")
                self.accountNumber = accountNumber
                return True
            else:
                print("Authentication Failed")
                return False
        else:
            print("Authentication Failed")
            return False
            
    def withdraw(self,withdrawalAmount):
        if withdrawalAmount > self.savingsAccount[self.accountNumber][1]:
            print("Insufficient Balance")
        else:
            self.savingsAccount[self.accountNumber][1] -= withdrawalAmount
            print("Withdrawal was successful.")
            self.checkBalance()
    
    def deposit(self, depositAmount):
        self.savingsAccount[self.accountNumber][1]+= depositAmount
        print("Deposit was successfule. Available balance: ")
        self.checkBalance()

    
    def checkBalance(self):
        print("Available balance: ",self.savingsAccount[self.accountNumber][1])


savingsAccount = SavingsAccount()
while True:
    print("Enter 1 to create a new account")
    print("Enter 2 to access an existing account")
    print("Enter 3 to exit")
    user = int(input())
    if user == 1:
        name = input("Enter your name: ")
        initialDeposit = int(input("Enter the initial deposit amount: "))
        savingsAccount.createAccount(name, initialDeposit)
    elif user == 2:
        name = input("Enter your name: ")
        accountNumber = int(input("Enter the Account Number: "))
        authenticationStatus = savingsAccount.validate(name, accountNumber)
        if authenticationStatus == True:
            while True:
                print("Enter 1 to withdraw ")
                print("Enter 2 to Deposit ")
                print("Enter 3 to check balance ")
                print("Enter 4 to go back to previous menu ")
                option = int(input())
                if option == 1:
                    withdrawalAmount = int(input("Enter the Withdrawal Amount"))
                    savingsAccount.withdraw(withdrawalAmount)
                elif option == 2:
                    depositAmount = int(input("Enter the Deposit Amount"))
                    savingsAccount.deposit(depositAmount)
                elif option == 3:
                    savingsAccount.checkBalance()
                elif option == 4:
                    break
    elif user == 3:
        quit()



