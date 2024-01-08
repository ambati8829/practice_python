#Abstraction - The process of handling complexity by hiding unnecessary information from user is called abstraction.
#Hiding internal functionality is also called as Abstraction.

#we can use Abstract classes for implementing abstraction.

#If a class contain one or more than one abstract method then the class is called abstract class.
#If the method is declared without implementation it is called as abstract method.

from abc import ABC, abstractmethod
class A(ABC):
    @abstractmethod
    def method(self):
        pass

obj1=A()
obj1.method()
#The above class is abstract class because it has one abstract method. We cannot instantiate abstract classes.
#The above code will give you this error:TypeError: Can't instantiate abstract class A with abstract method method

#Concrete Method:
#Normal method in abstract class is Concrete method, method2 is concrete method.
class A(ABC):
    @abstractmethod
    def method1(self):
        pass
    def method2(self):
        print("This is a concrete method.")
    @abstractmethod
    def method3(self):
        pass
#we cannot directly create object for Abstract class but we can inherit abstract class and we can create Object.
#Rules for inheriting abstract class: Abstract methods in abstract class must implement in subclass.

class B(A):
    def method1(self):
        print("Method1 is implemented in sub class.")
    def method3(self):
        print("Method3 is implemented in sub class.")

obj1=A()
obj1.method1()
obj1.method2()
obj1.method3()

#Abstract classes used as blueprint for another class. If a project has lof of classes and functions then developers create abstract class and use the classes by inheriting.
#if we want to define set of classes if the classes has common behaviour then we create abstract classes and derive Subclasses from it.
#when we are creating classes, if the classes have same methods and implementation is different then we create abstract class.











