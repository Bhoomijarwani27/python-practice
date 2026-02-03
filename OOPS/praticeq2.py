class employee:
    def __init__(self,role,dept ,salary):
        self.role = role
        self.dept = dept
        self.salary = salary
    def showdetails(self):
        print("role = ",self.role) 
        print("dept =",self.dept)  
        print("salary=",self.salary)

class engineer(employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("engineer","IT",100000)
    def showdetails(self):
        print("name =", self.name)
        print("age =", self.age)
        super().showdetails()    
# e1 = employee("python devloper","IT",180000)
# e1.showdetails()  
eg = engineer("bhoomi",20)
eg.showdetails() 