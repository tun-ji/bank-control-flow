class User:
    # This stores the users with their data - account = {'Name': name, 'Pin': pin, 'Tel': tel, 'Balance': balance}
    account = {}

    def __init__(self, uname, upin, tel, balance):
        self.account['Name'] = uname
        self.account['Pin'] = upin
        self.account['Telephone'] = tel
        self.account['Balance'] = balance

    # This function accepts how much you want to deposit as a float, adds it to your balance & then prints out the text
    def deposit(self):
        amount = float(input("How much would you like to deposit?"))
        print("You would like to deposit: " + str(amount))
        self.account['Balance'] += amount
        print("Your new balance is: " + str(self.account['Balance']) + ", " + self.account['Name'])

    # This function subtracts a specified amount from your balance if you have enough money then prints your new balance
    def withdraw(self):
        amount = float(input("How much would you like to withdraw?"))
        print("You would like to withdraw:" + str(amount))
        if self.account['Balance'] >= amount:
            self.account['Balance'] -= amount
            print("Withdrawal Successful\n Your new balance is: " + str(self.account['Balance']))
        else:
            print("Insufficient Balance")

    # The functions below print the attributes specified
    def view_tel(self):
        print(self.account['Telephone'])

    def view_pin(self):
        print(self.account['Pin'])

    def view_bal(self):
        print(self.account['Balance'])

    # The function below changes your telephone number to a user specified one
    def change_tel(self):
        print("Your current telephone number is " + str(self.account['Telephone']))
        self.account['Telephone'] = str(input("Please enter your new number: "))
        print("You've successfully changed your telephone number to: " + self.account['Telephone'])

    # This function changes your pin, but first checks to confirm that you own the account
    def change_pin(self):
        pin = input("Please enter your current pin")
        if pin == self.account['Pin']:
            self.account['Pin'] = str(input("Please enter your new pin: "))
            print("You've successfully changed your pin to: " + self.account['Pin'])

