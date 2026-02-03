class marks:
    def __init__(self , eng , maths , sci):
        self.eng = eng 
        self.maths = maths 
        self.sci = sci 
        # in oops it not need to mention data type but when you use combine then need 
        # self.percentage = str((self.eng +self.maths + self.sci) /3)+ "%"
    @property
    def percentage(self):
        return str((self.eng +self.maths + self.sci) /3)+ "%"

s1 = marks(88,90,78)
print(s1.percentage) 
s1.eng = 56
print(s1.eng)
print(s1.percentage)   # it not changed percentage 
# it can happen with function but need to write more things like call to print 
# it has @property method 
