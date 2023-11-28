class Person:
    
    num_of_object=0
    
    def __init__(self,name,age=22):
        self.name=name
        self.age=age
        Person.num_of_object+=1
    def __str__(self):
        return("hello {} you are {} years old".format(self.name, self.age))
        
        
        
person1 =Person("Najma", 24)
person2 =Person("Ali", 20)
person3 =Person("Ahmed")
#print the name
print(person1.name)
#print age:
print(person1.age)
#print all 
print(person1)
#to count the object
print("how many object we creat: ",person1.num_of_object)
#defualt value
print(person3.age)
        
        