# expense tracker using  list and dictionary if else  while loop  to track expenses basic functionality
expenses = []
print("WELCOME TO EXPENSE TACKER!")
while True:
     print("=======MENU======\n 1.Add Expense\n 2.view all expenses\n 3.View total spending\n 4.exit\n =================")
     choice = int(input("Enter your choice(1-4):"))
     if choice == 1:
          date = input("Enter the date of expense:")
          category = input("Enter the category : ")
          discription = input("Enter the discription:")
          Amount = float(input("Enter the amount:"))

          expense = {
               "date": date,
               "category": category,
               "discription": discription,
                "Amount": Amount
          }
          expenses.append(expense)
          print("Expense add sucessfully!")
     elif  choice == 2:
           if len(expenses)==0:
                print("No expense is recoreded.")
           else:
             print("List of expense:")
             count = 1
             for eachexpense in expenses:
                 print(f"{count}:{eachexpense['date']},{eachexpense['category']},{eachexpense['discription']},{eachexpense['Amount']}")
             count  = count + 1
     elif choice == 3:
         total = 0
         for eachexpense in expenses:
             total += eachexpense["Amount"]
         print("Total expense:",total)
     elif choice == 4:
         print("thank you!")
         break
     else: 
         print("Invaild!")
         

