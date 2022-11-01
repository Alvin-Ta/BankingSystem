from array import *


class account:
    bankAccNo = [["1001", "AlvinTa", 100.20],
                     ["2020", "junebuggy", 400.40],
                     ["1000", "junebug", 3000.21],
                     ["2021", "217896424", 100.12]]
    def fun(self):

        acc_no = input("Please enter your bank account number.\n")


        for i, element in enumerate(self.bankAccNo):

#            print(bankAccNo[i][0]) #print acc no
#            print(bankAccNo[i][1]) #print pass

            if self.bankAccNo[i][0] == acc_no:
                password = input("Please enter your password.\n")
                while password != self.bankAccNo[i][1]:
                    password = input("Wrong password, please try again.\n")

                if self.bankAccNo[i][1] == password:
                    ans = input("1. Deposit\n2. Withdraw\n")
                    if ans == "1":
                        amt = input("How much would you like to deposit?\n")
                        amt = int(amt)
                        self.bankAccNo[i][2] = deposit(self.bankAccNo[i][2], amt)
                        print("Your new balance is ${}" .format(self.bankAccNo[i][2]))
                        print("|---------------------------------------------|")
                    elif ans == "2":
                        amt = input("How much would you like to withdraw?\n")
                        amt = int(amt)
                        self.bankAccNo[i][2] = withdraw(self.bankAccNo[i][2], amt)
                        print("Your remaining balance is ${}" .format(self.bankAccNo[i][2]))
                        print("|---------------------------------------------|")

def deposit(total, amount):
    total += amount
    return total


def withdraw(total, amount):
    total -= amount
    return total






