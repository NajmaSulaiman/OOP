class Person:
    
    def __init__(self,name,gender,age=22):
        self.name=name
        self.age=age
        self.gender=gender
    def sayHi(self):
        print("hello {} from person class".format(self.name))
        
class Student(Person):
    def __init__(self,name,age=18):
        super().__init__(name,age)
    def sayHi(self):
        print("hello {} from Student class".format(self.name))
        
p1=Person("sara", 23)
s1=Student("Omar",18)
s2=Student("Hala")
s1.sayHi()
print(s2.age)
p1.sayHi()