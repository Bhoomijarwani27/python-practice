#polymorishm  : operator overloading 
#when the same opertor is allow to have different meaning according to context
print(2+2) #4
print("hello" + "world")#concatenate 
print([1,2,4,5]+[7,8,9,0]) #list merge  
# one operator + different use 
# it is implict overloding predefine by python 

# we can create our own 
class complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img 
    def showno(self):
        print(self.real, "i +", self.img ,"j")
    # dunder function means _ _add_ _ like this 

    def add(self,num2):
        newreal = self.real +num2.real
        newImg = self.img + num2.img
        return complex(newreal ,newImg)
    def __add__(self,num2):
        newreal = self.real +num2.real
        newImg = self.img + num2.img
        return complex(newreal ,newImg)
    def __sub__(self,num2):
        newreal = self.real -num2.real
        newImg = self.img - num2.img
        return complex(newreal ,newImg)
    #multiple
    def __mul__(self,num2):
        newreal = self.real *num2.real
        newImg = self.img * num2.img
        return complex(newreal ,newImg)
    #division 
    def __truediv__(self,num2):
        newreal = self.real /num2.real
        newImg = self.img / num2.img
        return complex(newreal ,newImg)
    #a%b
    def __mod__(self,num2):
        newreal = self.real %num2.real
        newImg = self.img % num2.img
        return complex(newreal ,newImg)
    





num1 = complex(1,3)
num2 =complex(4,9)
num1.showno()
num2.showno()
num3 = num1.add(num2) #without 
num3.showno()
num4 =num1 + num2 #with
num4.showno()
num4 =num1 - num2 #with sub 
num4.showno()
num4 =num1 * num2  
num4.showno()
num4 =num1 / num2  
num4.showno()
num4 =num1 % num2  
num4.showno()

                

                  