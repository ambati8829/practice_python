#Ability to use methods and attributes in a newly created class from already created class called Inheritance. OR Creating a new class from already created class.
#super class or base class or parent class is a already created class. Derived class or child class or sub class is created using the parent class.
#5 types of inheritance- Single Inheritance, Multiple Inheritance, Multilevel Inheritance, Hierarchical Inheritance, Hybrid inheritance.

#Single Inheritance
class Parent:
    def method1(self):
        print("I am a parent.")
        
class Child1(Parent):
    def method2(self):
        print("I am a child.")

child1=Child1()

child1.method2()
child1.method1()

#Multiple Inheritance
class Father:
    def method1(self):
        print("I am a father.")
class Mother:
    def method2(self):
        print("I am a mother.")

class Child2(Father, Mother):
    def method3(self):
        print("i am a child.")
child2 = Child2()

child2.method1()
child2.method2()
child2.method3()

#Multilevel Inheritance
class GrandParent:
    def method1(self):
        print("I am a grand parent.")
class Parent(GrandParent):
    def method2(self):
        print("I am a parent.")
        
class Child3(Parent):
    def method3(self):
        print("i am a child.")
child3 = Child3()

child3.method1()
child3.method2()
child3.method3()

#Hierarchical Inheritance
class Parent:
    def method1(self):
        print("I am a parent.")

class Child4(Parent):
    def method2(self):
        print("i am a first child.")

class Child5(Parent):
    def method3(self):
        print("i am a second child.")
        
child4=Child4()
child4.method2()
child4.method1()

child5=Child5()
child5.method3()
child5.method1()

#Hybrid Inheritance
class GrandParent:
    def method1(self):
        print("I am a grand parent.")
class Father(GrandParent):
    def method2(self):
        print("I am a father.")
class Mother:
    def method3(self):
        print("I am a mother.")

class Child6(Father,Mother):
    def method4(self):
        print("i am a child.")
        
child6=Child6()
child6.method4()
child6.method3()
child6.method2()
child6.method1()