class BankAccount:
    def __init__(self,balance,account_number):
        self.__balance=balance
        self.__account_number=account_number
        
    def deposit(self,deposit):
        self.deposit=deposit
        total=self.__balance+self.deposit
        
        return total
        
        
        
        
    def withdrawal(self,withdrawl):
        
        try:
            self.withdrawl=withdrawl
            if(self.withdrawl>0):
                total2=self.__balance-self.withdrawl
            
                return total2
            else:
                return "withdrawl can not be a negative  number"
        except:
            return ("something wrong ")
        
        
        
    def display(self):
        print("balance: {} account number: {}".format(self.__balance,self.__account_number))
        
        
account1=BankAccount(5000,90987)
account1.display()

print("balance after deposit: ",account1.deposit(50))
print("balance after withdrawal: ",account1.withdrawal(90))
print("balance after withdrawal: ",account1.withdrawal(-90))
print("balance after withdrawal: ",account1.withdrawal("g"))
