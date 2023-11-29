class Library:
    def __init__(self):
        self.book=[]
#         self.book2=[]
#         self.book3=[]
    def add_book(self,b):
        self.book.append(b)
#         self.book2.append(bb)
#         self.book3.append(bbb)
    def __str__(self):
        return "book name: {}. book author: {}. Number of copies: {}.".format(self.book[0],self.book[1],self.book[2])
    
    
    def search(self):
        
        
        
        
        
        
        
        
b1=Library()
b1.add_book("Python")
b1.add_book("muna")
b1.add_book(10)
print(b1)
"""
b2=Library()
b2.add_book2("Python")
b2.add_book2("sara")
b2.add_book2(10)
print(b2)

b3=Library()
b3.add_book3("Python")
b3.add_book3("ahmed")
b3.add_book3(10)
print(b3)"""