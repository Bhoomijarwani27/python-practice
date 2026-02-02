# 
set1 = {10 , "True" , "name" , 7.77}
print(set1)# different value allow
set2 = { 1 ,2,3, 4, 1}
print(set2)# repeat is not allow 

s = { 1, 45, 77, 234}
print(s)# index is not value can come changed postion

#s[2] = 30 not allow it not have index it unorder 

y = {}
print(type(y)) # it not set it dict
z = set() # use to create empty set 
print(type(z))# set 

# add 
set1.add(99)
print(set1)

print(len(set1))
#remove
s.remove(45) # if item not present error come
print(s)
s.discard(1)
print(s)
# in discard if value not present it will not give error

set2.clear() # use nto clear set 
print(set2) # all item romove if set is empty already no error come
set3 = { 1,3,88,98 }
set3.pop()
print(set3) # it remove random element

# add tuple
set3.add((1,7,8)) # it will add tuple it immutable
print(set3)
# add list 
#set3.add([1,4,8])# list cant add there item can change because it is mutable

s1 = set("bhoomi") # it will store each element separted remove duplicates
print(s1)
# union , difference
a = {'ram','shayam','jenny'}
b = {'jenny','jiya','Aakash'} 
c = {'reem','rahul'} 
print(a.union(b,c)) 
print(a | b |c) # other way of union
print(a.union(('mohon',"jenny"))) # tuple also happen with set here
# print(a | ('mohon',"jenny"))  not allow due to tuple
c.update(b) # it will add item of b in c
# c |= b other way to do update
print(c)
print("\n")
print(a.difference(b)) # a -b 
print(a - b)# otherway
# a.difference_update(b)
# print(a) element that are differnce has 
print(a.intersection(b)) # tell common 
a.intersection_update(b)
print(a)# now it has only intersection element
print("\n")
st1 = {'ram','shayam','jenny'}
st2 = {'jenny','jiya','Aakash'} 
print(st1.symmetric_difference(st2)) # give element that not prensent in both 
print(st1 ^ st2)# otherway
st1.symmetric_difference_update(b)
print(st1)
print("\n")
