class circle:
    def __init__(self,rad):
        self.rad = rad
    def area(self):
        return  3.14 * self.rad **2
    def perimeter(self):
        return 2*3.14*self.rad
           
c1 = circle(21)      
print(c1.area())
print(c1.perimeter())


