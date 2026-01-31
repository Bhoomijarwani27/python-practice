print('************ String Data Type ************')
# string is immutable it create other with same name 
 

coffee_type = "cold coffee"
print(coffee_type)
print(coffee_type[0])
first_char = coffee_type[0]
print(first_char)
slice_coffee = coffee_type[0:5] # it will print from index 0 to index 4 it will not include index 5
print(slice_coffee)
print(coffee_type[0:5])

num_list = "0123456789"
# slicing
print(num_list[:])
print(num_list[2:])
print(num_list[:5])
print(num_list[2:5])
print(num_list[0:10:1])
print(num_list[0:10:2])  # it will print alternate character in 2 it left one in 3 it will leave two character

coffee = "cold coffee"
print(coffee.replace("cold", "hot")) # it will replace cold with hot
print(coffee) # original string will not change because strings are immutable in python

coffee1 ="cold coffee, hot coffee, iced coffee"
print(coffee1)
print(coffee1.split(",")) # it will split the string at comma and return a list

print(coffee.find("ff")) # it will return the index of first occurrence of "ff"

print(coffee.find("C")) # it will return -1 because "C" is not found in the string it upper case in string that is lower case
print(coffee1.count("coffee")) # it will return the count of "coffee" in the string

#string to list 
coffee_type1 = "cold coffee"
quantity = "2 cups"
order = "I would like to have {} of {}"
print(order.format(quantity, coffee_type1)) # it will replace the placeholders with the values
 
 #list to string
coffee_varieties = ["cold coffee", "hot coffee", "iced coffee"]
print(coffee_varieties)
print(", ".join(coffee_varieties)) # it will join the list elements with comma and space
print(" | ".join(coffee_varieties)) # it will join the list elements with pipe symbol
print("-".join(coffee_varieties)) # it will join the list elements with hyphen

print(len(coffee_type1))

for char in coffee_type1:
    print(char)
... # it will print each character in the string on a new line

chai = "he said , \"masala chai is the best \" " # \ will that that string continue it use as "" it use as normal comma 
print(chai)

chai1 = "masala chai \n is the best" # \n is used to create a new line
print(chai1)
chai2 =  r"masala\n chai" # r is used to create a raw string it will not consider \n as new line
print(chai2)

# in window \ this is using As path 
# path = "C:\\newfolder\\testfile.txt\"  this is create error it consider AS window path 
path = r"C:\newfolder\testfile.txt" # r is used to create a raw string it will not consider \ as escape character
print(path)
print("masala" in chai) # it will return True because "masala" is present in chai
print("black" in chai) # it will return False because "black" is not present in chai

#multiline string
multiline_str = """This is a multiline string.
It can span multiple lines."""
print(multiline_str)

#string concatenation
str1 = "Hello"
str2 = "World"
str3 = str1 + " " + str2
print(str3) # it will concatenate str1 and str2 with a space in between
print(str1 + str2) # it will concatenate str1 and str2 without space
print(str1 + " " +str2)

#length of string
print(len(str1)) # it will return the length of str1

#indexing 
print(str3[0])

#upper case and lowercase
print(str3.upper()) # it will convert str3 to uppercase
print(str3.lower()) # it will convert str3 to lowercase
#title()
print(str3.title()) # it will convert str3 to title case it give first letter of each word in uppercase
#capitalize()
print(str3.capitalize()) # it will convert first letter of str3 to uppercase and rest to lowercase
#strip()
str4 = "   Hello World   "
print(str4)
print(str4.strip() + "hbh") # it will remove leading and trailing spaces (spaces at the beginning and end)
#lstrip()
print(str4.lstrip() + "hbh") # it will remove leading spaces (spaces at the beginning)
# #rstrip()
print(str4.rstrip() + "hbh") # it will remove trailing spaces (spaces at the end)
#find()
print(str3.find("ld")) # it will return the index of first occurrence of "World"
#replace()
print(str1.replace("ello", "yy")) # it will replace  "ello" with "yy" in str1
