
'''names = ["sd", "pd","ss", "rm"]
feedbacks = [3,4,4,5]
for i in range(len(names)):
    if (feedbacks[i] <4 ):
        print(names[i])
       print(feedbacks[i])'''

'''names=["P","Q","R", "S"]
fb=[4,5,2,4]
for i in range(0,4,1):
   if(fb[i]<5):
       print(names[i])'''

'''class Car:
    def __init__(self,make, model, year):
        self.make =make
        self.model =model
        self.year=year

    def start_engine(self):
        print("The engine has started. ")
my_car =Car(make='Toyota', model='Camry', year=2022)
print(my_car.make)
print(my_car.model)
print(my_car.year)'''

# A Sample Class with init method
class BankAccount:
    # init method or constructor
    def __init__(self, account_number, account_holder, balance):
        self.account_number=account_number
        self.account_holder=account_holder
        self.balance=balance

    def deposit(self, amount):
            self.balance += amount

    def withdraw(self, amount):
            if self.balance >= amount:
                self.balance -= amount
            else:
                print("Insufficient balance")

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate=interest_rate                                                                                                              
    def calculate_interest(self):
        return self.balance * (self.interest_rate / 100)                                                                                                        
# Example usage
account1 = SavingsAccount(12345,"Subhajit Datta", 1000,5)
account1.deposit(500)
account1.withdraw(200)
interest = account1.calculate_interest()
print(account1.balance)
print(interest) 
                                                                               
    




'''class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = str(account_holder)
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance >= amount:
           self.balance -= amount
        else:
            print("Insufficient balance")
class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate
    def calculate_interest(self):
        return self.balance * (self.interest_rate / 100)
# Example usage
account1 = SavingsAccount(12345, "hghdhd", 1500, 5)
account1.deposit(500)
account1.withdraw(200)
interest = account1.calculate_interest()
print(account1.balance)
print(interest)'''


















     


                        


        

       



    































































