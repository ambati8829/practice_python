#polymorphism -Having different forms. or An ability can do more than one task.
#Operator overloading - one Operator performing different in different cases. or One operator can handle more than one operation. Example - '+' operator, '*' operator.

#Operator overloading is an example of polymorphism.
#If a Function handles more than one datatype and different parameter size then it is polymorphism.

from multipledispatch import dispatch

class A:
    @dispatch(int,int)
    def add(self,a,b):
        print(a+b)
    
    @dispatch(int,int,int)
    def add(self,a,b,c):
        print(a+b+c)
    
    @dispatch(str,str)
    def add(self,a,b):
        print(a+b)
    
obj = A()
obj.add(1,2)
obj.add(1,2,3)
obj.add('sandeep','reddy')