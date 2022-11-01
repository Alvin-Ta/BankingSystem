from account import account
from register import register

user_ans = 1


while user_ans != 0:
    user_ans = input("Hello, please select one of the options below: \n1. Withdraw or deposit \n2. Register\nto exit, enter 0\n")
    if user_ans == '1':
        pee = account()
        pee.fun()

    elif user_ans == '2':
        val = register()
        val.addAnAccount()

    elif user_ans == '0':
        print("Have a great day!")
        break
