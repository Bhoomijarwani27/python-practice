# ask user input till it not between 1 to 10

while True:
     n = int(input("enter the number between 1 to 10:"))
     if 1 <= n <= 10:
          print("thanks")
          break
     else:
          print("try again") 
          