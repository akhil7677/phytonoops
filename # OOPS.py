# OOPS
# OBJECT ORIENTED PROGRAMMING LANGUAGE

# OOPS GIVES THE USER THE POEWER TO MAKE HIS OWN DATATYPES LIKE INT LIST ETC ETC

# making an atm machine class
class Atm:
    # constructor
    def __init__(self) -> None:
        
        print(id(self))
        # we have defined the data here
        self.pin=""
        self.balance=0
        self.menu()
        
        # what are the functions that can be used for 
        # the atm machines now
        # aka we are making functions now
        
    def menu(self):
        self.user_input=input("""Hi how can i help you ?
              1: press 1 to see balance
              2: press 2 to create pin
              3: press 3 to change pin
              4: press 4 to withdraw
              5: press 5 to fuck off ! :)
              """)
        
        if self.user_input=="1":
            self.check_balance()
    # check balance
        elif self.user_input=="2":
            self.make_pin()
        # create pin
        elif self.user_input=="3":
        # change pin
            self.change_pin()
        
        elif self.user_input=="4":
            self.withdraw()
        # withdraw
        
        elif self.user_input=="5":
            self.Lastoption()
        # well
        
        else:
            print("you pressed an unavaliable option so bye")
            exit()      
        
    # Balance check function
    def check_balance(self):
        self.balance=self.user_input=input("Enter your balance please :)") 
    # create pin function
    def make_pin(self):
        self.pin=self.user_input=input("Enter your pin")
    
    
    def change_pin(self):
        self.old_pin=input("enter the old pin")
        # checking if the old pin is equal to the new one
        if self.old_pin==self.pin : 
            self.newpin=self.user_input=input("Enter the new pin")
            # updating the old pin with the new one
            self.pin=self.newpin
        else:
            print("wrong pin entered")
        
        self.menu()
    
    def withdraw(self):
        # again askinng for the pin
        self.PinAtWithdrawl=self.user_input=input("enter the pin")
        if self.PinAtWithdrawl==self.pin:
            self.WithdrawalAmnt=print("enter the amounnt that has to be printed")
            if self.balance<self.WithdrawalAmnt:
                print("Asking for more amountb than avaliable so sorry .Redirecting to menu")
                self.menu()
            else:
                print(self.balance-self.WithdrawalAmnt)
                
    def Lastoption(self):
        self.user_input=input("WEll Fuck off boiiiii")
# object
obj=Atm()

