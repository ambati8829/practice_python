# 3 types of Methods: 1.Instance method 2.class Method 3.static method
#instance method: By default the methods we create in class are instance methods. Instance method is also called as Method of object.
# Instance methods create/access/modify/delete the objects attributes.
from types import MethodType

class Employee:
    def instanceMethod1(self):
        print("Instance Method created.")
    
    def instanceMethod2(self,a,b):
        print(a,b)
        
emp1 = Employee()
emp1.instanceMethod1()
emp1.instanceMethod2(20,30)

#creating instance variables using instance method
class Employee:
    A=200
    def __init__(self,name, empId, salary):
        self.name = name
        self.empId = empId
        self.salary = salary
    def getEmployeeName(self):
        print(self.name)  # this is how we can access variables in instance method.
        
    def getClassVariable(self):
        print(self.A) #To access class variable.
        
    def updateEmployeeName(self, new_name):
        self.name = new_name
        
    def updateClassVariable(self,new_value):
        self.__class__.A = new_value
    
    def deleteInstanceVariable(self):
        del self.name
    
    def deleteClassVariable(self):
        del self.__class__.A
        
emp1 = Employee("ambati",1,60000)
emp1.getEmployeeName()
emp2 = Employee("sandeep",2,60400)
emp2.getEmployeeName()
emp1.getClassVariable()
emp1.updateClassVariable(100)
print(Employee.A)
emp1.deleteInstanceVariable()
emp1.deleteClassVariable()


#creating instance method from outside
def addingMethod(self):
    print("Method added successfully from outside.")
    
emp1.newInstanceMethod = MethodType(addingMethod,emp1)
emp1.newInstanceMethod()