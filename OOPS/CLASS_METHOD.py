# class method
class person:
    name = "anonymous"
    
    def changeName(self,name):
        self.name = name 
    def change(self,name):
        #person.name = name    #person will change value in that name also  
        self.__class__.name = name  # this also doing same like that person. 

    @classmethod
    def NAME(cls, name): #it directally change the name with use of @classmethod
        cls.name = name

p1 = person()
p1.change("rahul") # name changed 
print(p1.name) # in this withiout person. it will not change name that it just give here 
print(person.name)

