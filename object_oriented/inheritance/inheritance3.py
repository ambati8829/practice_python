#removing duplicate from inheritance2.py using inheritance.
class Member:
    def __init__(self, firstName, lastName, email, memberId, address, mobileNo, dateJoined):
        self.firstName=firstName
        self.lastName=lastName
        self.email=email
        self.memberId=memberId
        self.address=address
        self.mobileNo=mobileNo
        self.dateJoined=dateJoined
    def getFullName(self):
        print(self.firstName+" "+ self.lastName)
    def changeAddress(self, newAddress):
        self.address = newAddress
        print(f"Address changed, new address is : {self.address}")
    def changeNumber(self, newNumber):
        self.mobileNo= newNumber
        print(f"Mobile number changes, new mobile number is : {self.mobileNo}")

class Faculty(Member):
    def __init__(self, firstName, lastName, email, memberId, address, mobileNo, subjectsTeaching, salary, dateJoined):
        self.subjectsTeaching=subjectsTeaching
        self.salary=salary
        Member.__init__(self, firstName, lastName, email, memberId, address, mobileNo, dateJoined)
    
    def getSalary(self):
        print(f"Your salary is {self.salary}")

class Student(Member):
    def __init__(self, firstName, lastName, email, memberId, address, mobileNo, subjectsLearning, GPA, dateJoined):
        self.subjectsLearning=subjectsLearning
        self.GPA=GPA
        Member.__init__(self, firstName, lastName, email, memberId, address, mobileNo, dateJoined)
    def getGPA(self):
        print(f"Your GPA is: {self.GPA}")