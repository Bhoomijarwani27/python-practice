tea_varties = ["black", "green", "oolong", "white"]
print(tea_varties)
print((tea_varties[0]))
print((tea_varties[-1]))
print(len(tea_varties))
# Changing the value of an item in a list
tea_varties[3] = "herbal"
print(tea_varties)
print(tea_varties[3])

#tea_varties[1:2]= "lemon" # ['black', 'l', 'e', 'm', 'o', 'n', 'oolong', 'herbal'] it will print each letter like array
tea_varties[1:2] = ["lemon"]
print(tea_varties)

#changing multiple values in a list // replacing 
tea_varties[0:2] = ["green", "matcha"]
print(tea_varties)

print(tea_varties[1:1]) # empty because it is starting and ending at same index and end index not print 
tea_varties[1:1] = ["chai", "earl grey"] # inserting values without replacing 
print(tea_varties)


tea_varties[1:3] = [] # removing values
print(tea_varties)
 
#  #looping through a list
for tea in tea_varties:
  print(tea, end="-")

# checking if an item is present in the list
if "masala" in tea_varties:
        print("\nMasala tea is available") #\n is for new line

tea_varties.append("masala") # adding value at the end of list
print(tea_varties)


tea_varties.pop()   # removing item from list last item
print(tea_varties)

tea_varties.remove("green") # removing specific item from list
print(tea_varties)

del tea_varties[2] # removing item at specific index
print(tea_varties)

tea_varties.insert(1, "herbal") # inserting item at specific index
print(tea_varties)

tea_varties_copy = tea_varties.copy() # copying a list
print(tea_varties_copy) # both lists are independent now if one changes other will not change

sqared_numbers = [x**2 for x in range(10)] # list comprehension
print(sqared_numbers) # it will print 10 numbers square from 0 to 9

cubed_numbers = [x**3 for x in range(5)] # list comprehension
print(cubed_numbers) # it will print 10 numbers cube from 0 to 5
