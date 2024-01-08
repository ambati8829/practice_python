#Encapsulation - Combining related things in to a single unit (combining data and methods in class)
#Advantages:
#1.Code will be organised and clean
#2.Prevents the data from accidental removal and deletion
#3. Abstraction(Hides implementation logic and allows only to use)
#4. Datahiding
#5. Modularity

#3 Access Specifiers:  Public, Protected and Private access specifiers

#If data is declared in public access specifier, we can access data 1)in same class 2)By Object 3)we can access from subclass&Access by subclass object.
#If data is declared in protected access specifier, it can access only that class and derived class.
#If data is declared as private access specifier. It can only access in that class.

#In python private and protected data is accessed same as public data.

#public access specifier
class Parent:
    publicData=10
    def publicMethod(self):
        print(self.publicData)

class Child(Parent):
    def method(self):
        print(self.publicData)
        
obj1=Parent()
obj1.publicMethod()
print(obj1.publicData)

obj2=Child()
obj2.method()
print(obj2.publicData)

#protected access specifier
class Parent:
    _protectedData=10
    def publicMethod(self):
        print(self._protectedData)

class Child(Parent):
    def method(self):
        print(self._protectedData)
        
obj1=Parent()
obj1.publicMethod()

obj2=Child()
obj2.method()

#private access specifier
class Parent:
    __privateData=10
    def publicMethod(self):
        print(self.__privateData)

class Child(Parent):
    def method(self):
        print(self.__privateData)
        
obj1=Parent()
obj1.publicMethod()


obj2=Child()
obj2.method()



