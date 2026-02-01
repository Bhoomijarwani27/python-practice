print(("Hello, world!" + "\n" ) *10)

#variable
x = "bhoomi"
print(f"hello {x}")
x = 10
# for x=10; x<10;x+1 {
#     print("hello bhoomi")
# }
print(id(x))
con = 20
print(id(con))

con = 10
print(id(con)) #in python it it store value not variable so  x and same memory address for same value like create a table 
# value referece  10     x, con
const = 9
print(id(con)) # now it will not  create new address for 20


const  = 100
const = x
print(const)
print(x) 
_a =100 
print(_a)
#assign multiple varible at time 
u , v ,w = 6 ,7 ,9 
print(u)
print(v)
print(u,v,w)
#multiple varible same value 
x = y = z = 100
print(x)
print(y)
print(z)
#swapping varible
a, b = 5, 10
a, b = b, a
print(a, b)

