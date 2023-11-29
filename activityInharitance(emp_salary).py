class Employee():
    
    def __init__(self,emp_id,emp_name,emp_salary,emp_assign_department):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.emp_salary=emp_salary
        self.emp_assign_department=emp_assign_department
        
        
        
    def __str__(self):
        return("{} {} {} {} ".format(self.emp_id,self.emp_name,self.emp_salary,self.emp_assign_department))
    
    def Calculate_emp_salary(self,hours):
        self.hours=hours
         
        
        if(self.hours> 50):
            overtime=self.hours-50
            overtime_amount=(overtime*(self.emp_salary/50))
            total=self.emp_salary+overtime_amount
            
            return total
        else:
            return self.emp_salary
        
        
            
        
        
    def set_assign_department(self,new_department):
        self.emp_assign_department=new_department
        
#     def get_assign_department(self):
#         print(self.emp_assign_department)
        
        
        
        
p1=Employee("Adams","E7876",50000,"ACOUNTING")
p2=Employee("JONES","E7499",45000,"RESEARCH")
p3=Employee("MARTIN","E7900",50000,"SALES")
p4=Employee("SMITH","E7698",55000,"OPREATIONS")
print(p1)
print(p2)
print(p3)
print(p4)
p1.set_assign_department("HR")
print(p1)
print("salary after overtime amount for ",p1.emp_id,p1.Calculate_emp_salary(55))
print("salary after overtime amount for ",p2.emp_id,p2.Calculate_emp_salary(60))
print("salary after overtime amount for ",p3.emp_id,p3.Calculate_emp_salary(40))
print("salary after overtime amount for ",p4.emp_id,p4.Calculate_emp_salary(50))