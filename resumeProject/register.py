from account import account
import random


class register:

    def addAnAccount(self):
        bankAccountNum = random.randint(1000, 9999)
        bankAccountNum = str(bankAccountNum)
        print("Your accout number is {}" .format(bankAccountNum))
        password = input("Please set your bank account password\n")
        amount = input("Please deposit money into your account (min $100)\n")
        amount = int(amount)
        while amount < 100:
            amount = input("Please enter an amount greater or equal to $100\n")
            amount = int(amount)

        newAccount = [bankAccountNum, password, amount]
        createdAccount = account()
        createdAccount.bankAccNo.append(newAccount)
        print("Your account has been added.")