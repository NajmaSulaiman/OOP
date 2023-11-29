class Number():
    def __init__(self):
        self.numbers=[]
    
    def add_num(self,num):
        self.numbers.append(num)
        
    def sum_num(self):
        sum1=0
        for i in self.numbers:
            sum1+=i
        return sum1
    
n1= Number()
n1.add_num(2)
n1.add_num(3)
print(n1.sum_num())
