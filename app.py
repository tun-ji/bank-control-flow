from bank import Bank
from user import User


# This is used to instantiate a new Bank object
bank = Bank()

print("Welcome to The Bank \n What would you like to do?")
active = 0
while active == 0:
    print("[1] Create an Account")
    print("[2] Log in to your account")
    print("[3] Exit")

    task = int(input())
    if task == 1:
        # This is where new students are instantiated
        user = User(str(input("What is your name?")), str(input("Choose a pin")), str(input("Please enter your phone number")), float(input("What's your balance?")))
        bank.updater(user)
        print(user.account['Name'] + ", your account has been created successfully")
    elif task == 2:
        print("Please enter your account details")
        name = input("What is your name?")
        pin = input("Please enter your pin")
        reg_user = bank.login(name, pin)
        if reg_user:
            print("Welcome " + name)
            acc_state = 1
            while acc_state == 1:
                # This could've been better implemented with the Python equivalent of a switch statement
                print("What would you like to do?")
                print("[1] Deposit Money")
                print("[2] Check Balance")
                print("[3] Withdraw Money")
                print("[4] Change Phone Number")
                print("[5] Change PIN")
                print("[6] Go Back")
                opt = str(input())
                if opt == "1":
                    reg_user.deposit()
                elif opt == "2":
                    reg_user.view_bal()
                elif opt == "3":
                    reg_user.withdraw()
                elif opt == "4":
                    reg_user.change_tel()
                elif opt == "5":
                    reg_user.change_pin()
                elif opt == "6":
                    acc_state = 0
                else:
                    print("Please choose one of the options")
        else:
            print("Account not found")
            continue
    elif task == 3:
        print("Thanks for banking with us!")
        exit()
        active = 0
