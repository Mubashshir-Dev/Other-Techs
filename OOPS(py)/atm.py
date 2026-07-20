

class Atm:
    def __init__(self):
        self.pin=""
        self.balance=0

        self.menu()
    def menu(self):
        user_input=input("""
                                 hello how would you like to proceed
                                1. Create PIN
                                2. Deposit
                                3. withdraw
                                4. check balance
                                5. Exit 
                         """)
        if user_input=="1":
            self.create_pin()
        elif user_input=="2":
            self.deposit()
        elif user_input=="3":
            self.withdraw()
        elif user_input=="4":
            self.balance_check()
        elif user_input=="5":
            self.quit_atm()
        else:
            self.quit_atm()
    def create_pin(self):
        if(self.pin==""):
            self.pin=input("enter your pin")
            print("pin set successfully")
        else:
            temp=input("prev pin")
            if(temp==self.pin):
                self.pin=input("enter your pin")
                print("pin set successfully")
            else:
                print("incorrect pins")

        
    def deposit(self):
        temp = input("enter pin : ");
        if(temp==self.pin):
            self.balance+=int(input("enter amount "))
            print(self.balance)
        else:
            print("wrong pin")

    def withdraw(self):
        temp=input("pin : ")
        if(temp==self.pin):
            amount = int(input("amount to withdraw"))
            if(amount>self.balance):
                print("maximum you can withdraw is ",self.balance)
            else:
                self.balance-=amount
                print(self.balance," lefted")
        else:
            print("wrong pin")
        
    def balance_check(self):
        temp=input("pin")
        if(temp==self.pin):
             print(self.balance," lefted")
        else:
            print("wrong pin")
        
    def quit_atm(self):
        pass

sbi = Atm()