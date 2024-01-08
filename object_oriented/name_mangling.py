#NameMangling- Declare data or method with atleast 2 leading underscores and atmost 1 trailing underscore. Then it will replace to _classNameName by the interpreter.

#In python if we declare data ass private member then it is accessible only in that class. To access that member, this NameMangling is introduced.

class A:
    __a = 10
    ___b=23
    ____c=45
    _____d=34
    __e_=45
    __f__=76
    __g___=43
    ____h_=67
    _i_=90

#print(dir(A))
#the above print statement will print 
#['_A_____d', '_A____c', '_A____h_', '_A___b', '_A__a', '_A__e_', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__f__', '__format__', '__g___', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_i_']
#Only the variables which satify the statement in the 1st line, modified because of NameMangling.

#to access these private variables.

class A:
    __a = 10
    ___b=23
    ____c=45
    _____d=34
    __e_=45
    __f__=76
    __g___=43
    ____h_=67
    _i_=90
    
    def getPrivateData(self):
        print(self.__a)

class B(A):
    def getPrivateMember(self):
        print(self._A__a)
    
obj1= A()
print(obj1._A__a)

obj2=B()
obj2.getPrivateMember()
print(obj2._A__a)