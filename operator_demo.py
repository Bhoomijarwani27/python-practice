# 1. arithmetic operators
# + , - , * , / , % , ** , //
a = 10
b = 3  
print("a + b = ", a + b)  # addition
print("a - b = ", a - b)  # subtraction 
print("a * b = ", a * b)  # multiplication
print("a / b = ", a / b)  # division
print("a % b = ", a % b)  # modulus
print("a ** b = ", a ** b)  # exponentiation
print("a // b = ", a // b)  # floor division

# 2. assignment operators
# = , += , -= , *= , /= , %= , **= , //=
c = 5
c += 2  # c = c + 2
print("c += 2 : ", c)   
c -= 2  # c = c - 2
print("c -= 2 : ", c)
c *= 2  # c = c * 2
print("c *= 2 : ", c)
c /= 2  # c = c / 2
print("c /= 2 : ", c)
c %= 2  # c = c % 2
print("c %= 2 : ", c)
c **= 2  # c = c ** 2
print("c **= 2 : ", c)
c //= 2  # c = c // 2
print("c //= 2 : ", c)
b <<= a
print("b <<= a : ", b)

# 3. comparison operators   / relational operators
# == , != , > , < , >= , <=
x = 10
y = 20
print("x == y : ", x == y)  # equal to
print("x != y : ", x != y)  # not equal to
print("x > y : ", x > y)    # greater than
print("x < y : ", x < y)    # less than
print("x >= y : ", x >= y)  # greater than or equal to
print("x <= y : ", x <= y)   # less than or equal to

# 4. logical operators
# and , or , not
p = True
q = False
print("p and q : ", p and q)  # logical AND
print("p or q : ", p or q)    # logical OR
print("not p : ", not p)      # logical NOT
print("not q : ", not q)      # logical NOT

# 5. bitwise operators
# & , | , ^ , ~ , << , >>
m = 5  # binary: 0101
n = 3  # binary: 0011
print("m & n : ", m & n)  # bitwise AND
print("m | n : ", m | n)  # bitwise OR
print("m ^ n : ", m ^ n)  # bitwise XOR
print("~m : ", ~m)        # bitwise NOT
print("m << 1 : ", m << 1)  # left shift
print("m >> 1 : ", m >> 1)  # right shift

#walrus operator 
# help in assign with use 
a = True 
print(a := False ) 
# it help to do code in less line 
numbers = [1 , 2, 3, 4, 5]
while (n := len(numbers)) >0: # in this we made new variable in while with help of warlus it assign and check 
    print(numbers.pop())
    # it will return whhich element pop 

f = float(input())
f = f*10
print(f)