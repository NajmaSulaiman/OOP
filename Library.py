class Library:
    
    def __init__(self):
        self.library=[]
        
        
    def add_book(self,tital,auther,copies):
        book={"Tital":tital,"Auther":auther,"Copies":copies}
        self.library.append(book)
        
    def display_book(self):
        for i in self.library:
            print(i)
    
    def search_book(self,tital):
        for i in self.library:
            if(i["Tital"] == tital):
                print(i["Auther"])
        
        
        
        
        
        
        
lb1=Library()
lb1.add_book("python","Tom","11")
lb1.add_book("C++","JOHN","3")
lb1.add_book("JAVA","RIE","7")
lb1.display_book()
lb1.search_book("python")



        
    