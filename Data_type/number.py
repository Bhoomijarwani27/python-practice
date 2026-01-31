username = "user123"
print(username[-1])
print(username[0:4])
 
  # numbers 

x = 2
y =3
z = 4
print(x + y)
print(x ** y)
print(y**z)
print(y**x) # exponentiation first element will multiple by itself second element tell how many times

#  x +y * z not allow to do this without parentheses it not right way to write code
print((x+y)*z) # correct way to write code with parentheses
print(x,y,z)
print( x+ 1, y+ 1, z+ 1)
print (2**1000) # python can handle big numbers
repr("hello")  # use to identify the data type 
str("hello") # use to describe the data type for human understanding
print(repr("hello")) 
print(str("hello"))
print("hello") # take value to show on screen 

import math
from unicodedata import decimal # it provide decimal value of unicode character
print(math.ceil(2.3)) # it give higher value
print(math.floor(2.9)) # it give less value 
print(math.floor(-2.9)) # it give smaller value i n negative number -3 is smaller than -2.9 
print(math.trunc(-2.9)) # it just remove decimal part
print(math.trunc(2.9)) # it just remove decimal part

 # complex numbers
 #  j is used to represent imaginary part of complex number
print( 1 + 2j)
print((1 + 2j)*3)

#oct , hex , bin 
print(0o10) # octal representation of 8
print(0xff) # hexadecimal representation of 255
print(0b1000) # binary representation of 8
print(oct(100)) # octal representation of 100
print(hex(19)) # hexadecimal representation of 19
print(bin(64)) # binary representation of 64
print(bin(77))

# decimal has 0-9 number total 10 numbers it used AS int to covert oct , hex , bin to decimal (integer)
# covert 
print(int('64',8)) # convert octal string to integer
print(int('69',16)) # convert hexadecimal string to integer
print(int('100',2)) # convert binary string to integer

import random
print(random.random()) # it give random number between 0 to 1

print(random.randint(1,100)) # it give random integer between 1 to 100  

l1 =["blue", "red", "green", "yellow"]
print(random.choice(l1)) # it give random choice from list always give different output to each run
print(random.choice(l1)) # it give random choice from list

random.shuffle(l1) # it shuffle the list randomly
print(l1)

print((0.1 +0.1  + 0.1) - 0.3) #5.551115123125783e-17 # it show precision error in floating point arithmetic
 # to avboid this use decimal module (libreary)
from decimal import Decimal
print((Decimal('0.1') + Decimal('0.1') + Decimal('0.1')) - Decimal('0.3')) # it give exact result using decimal module

from fractions import Fraction
myFra = Fraction(3,4) 
print(myFra) # it show fraction 3/4

setone = {1,2,3,4,5}
settwo = {4,5,6,7,8}
print(setone & settwo)  # intersection
print(setone | settwo) # union 
print(setone - settwo) # difference
print({1,2} - {1,2}) # empty set
print(setone ^ settwo) # symmetric difference # elements in either setone or settwo but not in both

# boolean
print(True == 1)
print(False == 0)
print(True + 4) # it treat True as 1


