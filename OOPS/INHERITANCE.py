# inheritance = parent child class 
# types 
#single inheritance 
# multi-level inhertance
# mutliple inhertance 
class student:
    def __init__(self,name ,enroll):
       self.name = name 
       self.enroll = enroll
class first(student):
     def __init__(self, name, enroll,rollno):
         super().__init__(name, enroll)
         self.rollno = rollno
          
s1 = first("jghj" ,"12345" ,"12")
print(s1.name)  
print(s1.enroll)  
print(s1.rollno)  
#muti-level means it access other  that is just up her and  indirectly  access all 
#like 1 -> 2 ->3 not 1-> 3 it happen indircetly 
class Car:
    def __init__(self, car_type):
        self.type = car_type

    def start(self):
        print("Car started")


class ToyotaCar(Car):
    def __init__(self, car_type, brand):
        super().__init__(car_type)   # call Car constructor
        self.brand = brand


class Fortuner(ToyotaCar):
    def __init__(self, car_type, brand, name):
        super().__init__(car_type, brand)  # call ToyotaCar constructor
        self.name = name


# object creation
car1 = Fortuner("Diesel", "Toyota", "Fortuner")

car1.start()
print(car1.type)
print(car1.brand)
print(car1.name)
  

#multiple inheritance 

class A:
    varA = "welcome to A class"
class B:
    varB = "welcome to B class"  
class c(A,B):
    varC = "welcome to C class"
c1 = c()
print(c1.varA)
print(c1.varB)
print(c1.varC)
