class Person():
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
        
    @classmethod
    def years(cls,name, byears):
        age=2023-byears
        return cls(name,age)
    
    
p1=Person.years("ahmed",1999)
print("age : ",p1.age)
