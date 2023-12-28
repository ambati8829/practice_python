#If the class contains more than one method with a same name and the methods contain different datatypes of parameters or different no.og parameters or both is called as Method overloading. 

import multipledispatch

class A:
    @multipledispatch.dispatch(int,int)
    def add(self,a,b):
        return a+b
    
    @multipledispatch.dispatch(int,int,int)
    def add(self,a,b,c):
        return a+b+c
    
    @multipledispatch.dispatch(str,str)
    def add(self,a,b):
        return a+b
    
obj = A()

print(obj.add(1,2))
print(obj.add(12,3,4))
print(obj.add('sandeep','ambati'))
