# abstraction = hidding things 
class car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    def start(self):
        self.acc = True
        self.clutch = True
        print("car start ")
p1 = car()
print(p1.acc) # before vALUE of fun 
p1.start()# fun call 
print(p1.acc) # value come from fun 


#encapsulation = wrapping data and function in single unit(object)
class Account:
    def __init__(self,bal , acc):
        self.balance = bal 
        self.account_no = acc
    def debit(self ,amount):
        self.balance -= amount
        print("Rs.", amount , "was debited") 
        print("Total balance = ",self.get_balance())
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount , "was credited") 
        print("Total balance = ",self.get_balance())  
    def get_balance(self):
        return self.balance

myacc = Account(100000,123)    
myacc.debit(45)
myacc.credit(90)    
myacc.credit(45)

