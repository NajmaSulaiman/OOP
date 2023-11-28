class Person:
    
    num_of_object=0
    
    def __init__(self,name,age=22):
        self.__name=name
        self.__age=age
        Person.num_of_object+=1
        
    def set_name(self,new_name):
        self.__name=new_name
        
    def get_name(self):
        #return self.__name
        print(self.__name) 
    
    
    def __str__(self):
        return("hello {} you are {} years old".format(self.__name, self.__age))
    
    def talk(self):
        return ("{} is talking".format(self.__name))
        
        
        
person1 =Person("Najma", 24)
person2 =Person("Ali", 20)
person3 =Person("Ahmed")
#set
person2.set_name("Muna")
#person2.get_name()
print(person2)
"""
#print the name
print(person1.name)
#print age:
print(person1.age)
#print all 
print(person1)
#to count the object
print("how many object we have creat: ",person1.num_of_object)
#defualt value
print(person3.age)
print(person3.talk())
        """
        