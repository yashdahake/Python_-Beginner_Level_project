class Atm:
    def __init__(self):
        self.pin=" "
        self.balance=0
        self.menu
        
    def menu(self):
        user_input=input('''
                    Hello,how would you like to procced?
                    1.Enter 1 to create pin
                    2.Enter 2 to deposit
                    3.Enter 3 to Withdraw
                    4.Enter 4 to check balance
                    5.Enter 5 to Exit
                    ''')
        if user_input=="1":
            self.Create_pin()
        elif user_input=="2":
            self.deposit()
        elif user_input=="3":
            self.withdraw()
        elif user_input=="4":
            self.check_balance()
        else:
            print("BYE THANKYOU")
            
    def Create_pin(self):
        self.pin=input("Enter Your Pin :")
        print("Pin set successfully")
    def deposit (self):
        temp=input("Enter Your Pin :")
        if temp==self.pin:
            amount=int(input("Enter Amount :"))
            self.balance=self.balance+amount
            print("Deposit successful")
        else:
            print("Invalid Pin")
    def withdraw(self):
        temp=input("Enter Your Pin :")
        if temp==self.pin:
            amount=int(input("Enter Amount :"))
            if amount<self.balance:
                self.balance=self.balance-amount
                print("Operation Successful")
            else:
                print("Insufficien funds")
        else:
            print("Invalid Pin")
    def check_balance(self):
        temp=input("Enter Your Pin :")
        if temp==self.pin:
            print(self.balance)
        else:
            print("Invalid Pin")

sbi=Atm()
sbi.Create_pin()