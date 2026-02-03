class food: # name of class
    snacks = "pizza" # class attribute
    drinks =" coke"
    def __init__(self): # default constructor 
        pass
# creating object of class
obj = food()
# accessing class attribute using object    
print("My favorite snack is:", obj.snacks)
print(obj.drinks)


class car:
    def __init__(self,brand , model, RS): # parameterzied  constructor 
       self.brand = brand
       self.model = model 
       self.RS = RS
    def full_name(self):
        return f"{self.brand} {self.model}"   
RS = input("enter the price of car")
my_car = car("toyoto", "corolla",RS)
print(my_car.brand)
print(my_car.model)
print(my_car.RS)
print(my_car.full_name())

class drink:
    def __init__(self):
          self.soft_drink = input("your Fav drink: ")
my_drink = drink()
print("my fav  soft drink is:", my_drink.soft_drink)