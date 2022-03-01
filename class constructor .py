# creating a constructor class
class Employee:
    def __init__(self,name,age,salary,gender):
        self.name=name
        self.age=age
        self.salary=salary
        self.gender=gender
        
    def Show_details(self):
        print(f"Name of Empolyee is {self.name}")
        print(f"Age of Empolyee is {self.age}")
        print(f"Salary of Empolyee is {self.salary}")
        print(f"Gender of Empolyee is {self.gender}")
    
ob=Employee("Yuvraj Verma",21,4500000,"Male")

ob.Show_details()