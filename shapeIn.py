class Shape:
    
    def __init__(self,color,name):
        self.color=color
        self.name=name
        
    
    def __str__(self):
        return("the color of the shape: {} and the name: {}".format(self.color,self.name))
    
    def Area(self):
        print("the are of the shape is ")
        
class Squer(Shape):
    def __init__(self,color,name,l):
        super().__init__(color,name)
        self.l=l
        
    def Area(self):
        #l=int(input("enter the lenth of the sequer: "))
        area=self.l**2
        return area
        
        #print("the are of the sequer is ",self.area)
    def __str__(self):
        return("the color of the Squer: {} and the name: {} ".format(self.color,self.name))
    
class Circle(Shape):
    def __init__(self,color,name,r):
        super().__init__(color,name)
        self.r=r
    def Area2(self):
        #r=int(input("enter the radus of the sequer: "))
        area2=(3.14*(self.r**2))
        
        return area2
        #print("the are of the sequer is ",self.area)
    def __str__(self):
        return("the color of the Circle: {} and the name: {}  ".format(self.color,self.name))
    
    
shape1=Shape("Black","shape1")
s1=Squer("Orange","Squer1",8)
c1=Circle("Pink","Circle1",3)
print(shape1)
print(s1)
print(c1)
print("the area of the squer: ",s1.Area())
print("the area of circle: ",c1.Area2())
#c1.Area2()
    