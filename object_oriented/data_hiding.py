#DataHiding- Declare data in one class, doesn't give access to another class & hides the data.(Hides sensitive information fro security purpose)

class Bank:
    __balance=10000
    def getBalance(self):
        return self.__balance

class API(Bank):
    def printBalance(self):
        return self.__balance

obj= API()
print(obj.getBalance())
print(obj.printBalance())