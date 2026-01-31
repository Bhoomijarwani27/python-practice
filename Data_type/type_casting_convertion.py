# type casting
#convert one data type to another data type 
# explicit type conversion (manual type conversion by programmer) / type casting
a= "1"
b = "2"
print(a+b)  # it will take as string so it will not perform addition it will perform concatenation 

print(int(a)+int(b))  # it will convert string to integer and perform addition

# only int will convert into int like happy will not covert into int it will give error

c = 1 
d = 2
print(str(c)+ str(d)) 
# implicit type conversion (automatic type conversion by python interpreter) / type conversion
p = 1.5 
q = 2
print(p+ q)  # it will automatically convert int to float and perform addition


#practice
c = input("enter temperature in celsius: ")
f = (int(c) * 9/5) + 32
print("Fahrenheit value is: ", f)
 
k = int(c) + 273.15
print("Kelvin value is: ", k)