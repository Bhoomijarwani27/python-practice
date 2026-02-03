class student:
    def __init__(self,name):
        self.name = name 
s1 = student("bhoomi")
print(s1.name)
del s1 # use to delet object     

#private(like) attributes and methods
# conceptual implementation in python 
class Account:
    def __init__(self,acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass # by adding __ 2 underscore in starting it become private
    def reset_pass(self):
        return(self.__acc_pass)  # it will work here it class 

myacc = Account("123", "gfghghfh")  
print(myacc.acc_no)
# print(myacc.__acc_pass) 
print(myacc.reset_pass())
class person:
    __name = "ghjgv" # private 
    def __hello(self):
        return ("hello")
    def welcome(self):
         return self.__hello() # use in other function is allow 
        
p1 = person()
# print(p1.__name)    it will not work 
# print(p1.__hello()) it will not work  
print(p1.welcome()) # it will work here 

# supper method is related to inhertaince so it in inhertance file 


#class method 