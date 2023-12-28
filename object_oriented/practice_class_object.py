#In Python, Everything is Object.
#OOPS - Object Oriented Programming System
#OOPS is a programming paradigm. This a an Approach/Method/Strategy/Style/Model for solving a problem or task.
# Everything in this world is an Object. Objects have both properties and behaviour. Suppose, take me as an Object: My properties would be My name, DOB, Gender, Height, Weight. My Behaviour are all the works I am doing. 
#In coding, these properties are called as Attributes or Variables. Behaviour is called as Methods or Procedures.
#OOPS concepts: Class, Object, Inheritance, Polymorphism, Encapsulation, Abstraction
#Class - Blue print for creating object.
#Example Bank Account Program- Attributes: Bank Account Number, Name, IFSE Code, Balance. Methods or Behaviour: Withdraw, Deposit, Check Balance

class BankAccount:
    def __init__(self, accountNo, accountName, ifseCode, balance):
        self.accountNo = accountNo
        self.accountName = accountName
        self.ifseCode = ifseCode
        self.balance = balance
    def withdraw(self, amount):
        self.balance-=amount
    def deposit(self, amount):
        self.balance+=amount
    def checkBalance(self):
        print(self.balance)
        
        
obj1 = BankAccount(123,"Ambati", "Mar1111", 200000)
obj1.checkBalance()
obj1.deposit(40000)
obj1.checkBalance()
obj1.withdraw(200000)
obj1.checkBalance()