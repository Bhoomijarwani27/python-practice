# print tables  skip 5 to print 
i = 1
n = int(input("enter the number:"))

while i <= 10:
    if i == 5:
        i +=1
        continue  
    print(f"{n} x {i} = {n*i}")
    i = i+1


