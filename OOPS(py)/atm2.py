

class Atm:
    def __init__(self):
        self.__pin=""
        self.__balance=0

        self.__menu()
    def get_pin(self):
        return self.__pin
    def set_pin(self,new_pin):
        if(type(new_pin)!=str):
            print("Not allowed")
        else:
            self.__pin=new_pin
    def __menu(self):
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
        if(self.__pin==""):
            self.__pin=input("enter your pin")
            print("pin set successfully")
        else:
            temp=input("prev pin")
            if(temp==self.__pin):
                self.__pin=input("enter your pin")
                print("pin set successfully")
            else:
                print("incorrect pins")

        
    def deposit(self):
        temp = input("enter pin : ");
        if(temp==self.__pin):
            self.__balance+=int(input("enter amount "))
            print(self.__balance)
        else:
            print("wrong pin")

    def withdraw(self):
        temp=input("pin : ")
        if(temp==self.__pin):
            amount = int(input("amount to withdraw"))
            if(amount>self.__balance):
                print("maximum you can withdraw is ",self.__balance)
            else:
                self.__balance-=amount
                print(self.__balance," lefted")
        else:
            print("wrong pin")
        
    def balance_check(self):
        temp=input("pin")
        if(temp==self.__pin):
             print(self.__balance," lefted")
        else:
            print("wrong pin")
        
    def quit_atm(self):
        pass

sbi = Atm()
