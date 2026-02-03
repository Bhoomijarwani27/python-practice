class student:
    @staticmethod # it use to avold self it not need that self so use with staticmethod 
    # it is decorator @staticmethod 
    # can't  access or modify class state and generally for utilty 
    def fun():
        return "hello"
s1 = student()        
print(s1.fun())
print(student.fun()) # it not have self so call with class name allow

