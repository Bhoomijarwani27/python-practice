# in python it done by : in other {} 
# writing in file is global 
x = "global" # G (Global)

def outer():
    x = "enclosing" # E (Enclosing)
    def inner():
        x = "local" # L (Local)
        print("Inner:", x)
    
    inner()
    print("Outer:", x)

outer()
print("Global:", x)



s , y  = input("enter two value: ").split() 
print(s)
print(y)
