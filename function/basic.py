# function  2 type  
#  function used when we need same block of code again agin we make function then just need to call function 
# 1. build in like print()
# 2.  user define 
name = input("enter your name:")
def greet():
    print(f"hello {name}!")
    print("good morining!")
    print("Have a nice day!")
def colour ():
    colour = input("enter your fav colour:")   
    print("your fav colour is: ",colour) 

greet()  #it will print greet function with your name 
colour()    


# function parameter 
def maths(a,b):
    s = a + b
    avg = s / 2
    sq = a ** 2
    print("sum:", s)
    print("avg:", avg)
    print("square of a: ",sq)


#function calling with argument
maths(2,8)
a  = int(input("enter the value of a  for sum and averge:"))
b = int(input("enter the value of b  for sum and averge:"))
maths(a,b )

def multiply(n1 = 10 , n2 = 10):# if value not give then it take default
    return n1* n2
result = multiply(6,9 )
print(result)