#3 types of variables - 1.static variables or class variable 2.instance variable 3.local variable
#Local variable: The variable which is declared inside the method is called Local Variables.(same as variable declaration in function.)
#static or class variable: The variable which is declared outside the method and inside the class.

#Static Variable
class A:
    staticVariable1 = 10
    staticVariable2 = 20
    
    def sampleMethod(self):
        print("sample method")
        
A.staticVariable3 = 30 #can create the static variables this way as well.
obj = A()
print(obj.staticVariable1)

#Instance Variable
class A:
    def __init__(self,a,b):
        self.instanceVariable1 = a 
        self.instanceVariable2 = b
    def updateVariable(self,newValue):
        self.instanceVariable1 = newValue

obj = A(2,3)
obj.instanceVariable3= 40
obj.instanceVariable4= 50
obj.updateVariable(400)
print(obj.instanceVariable1)

#Example:
class Student:
    schoolName = "ABC" #class variable or static variable
    
    def __init__(self,name,rollNo,address,phoneNo):
        self.name = name # instance variable
        self.rollNo = rollNo # instance variable
        self.address = address # instance variable
        self.phoneNo = phoneNo # instance variable

s1 = Student('A',1,'a',3456)
s2 = Student('B',2,'fs',345645)
s3 = Student('C',3,'f',345633)
s4 = Student('D',4,'agt',345699)

Student.schoolName = "XYZ"

for obj in [s1,s2,s3,s4]:
    print(obj.name)
    print(obj.rollNo)
    print(obj.address)
    print(obj.phoneNo)
    print(obj.schoolName)