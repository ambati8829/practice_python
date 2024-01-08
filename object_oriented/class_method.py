#class methods: To perform operations on class variables we create in class method
#we cannot access instance variables using class methods.
#We can access class variables using objects and access using class.
#Class method can be accessed using object and accessed using class.
#Class methods not only used for accessing class variables but also used to deal with factory methods.
#Why we create class method? - To perform operations on class level variables and to deal with factory methods.

class Student:
    @classmethod
    def classMethod1(cls):
        print("class method created")
        
Student.classMethod1()
student1 = Student()
student1.classMethod1()

#To access class variables
class Student:
    college = 'ABC'
    
    @classmethod
    def classMethod1(cls):
        print(cls.college)

Student.classMethod1()
student1 = Student()
student1.classMethod1()

#Updating class variables using class methods.
class Student:
    college = 'ABC'
    
    @classmethod
    def classMethod1(cls, new_value):
        print(cls.college)
        cls.college = new_value
        print(cls.college)

Student.classMethod1('XYZ')
student1 = Student()
student1.classMethod1('GIT')

#deleting class variable using class methods
class Student:
    college = 'ABC'
    
    @classmethod
    def classMethod1(cls):
        print(cls.college)
        del cls.college
        
Student.classMethod1()

#Factory Methods - These are used to create object using method. or Used to create class Instance.
#Factory method work as alternate constructor.

import datetime
class Student:
    def __init__(self,name,id,age):
        self.name = name
        self.id = id
        self.age = age
    
    @classmethod
    def getAgeAsDob(cls,name,id,age):
        return cls(name, id, datetime.datetime.now().year-age)

student1 = Student.getAgeAsDob("Rakesh",2345,2003)
print(student1.name, student1.id, student1.age)
student2 = Student("AMBATI",455,25)

student3 = Student.getAgeAsDob("sandeep",34,1997) 