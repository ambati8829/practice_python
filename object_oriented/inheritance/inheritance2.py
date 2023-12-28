#Inheritance is introduced to remove code duplication, to maintain relationship between Objects.

class Faculty:
    def __init__(self, firstName, lastName, email, facultyId, address, mobileNo, subjectsTeaching, salary, dateJoined):
        self.firstName=firstName
        self.lastName=lastName
        self.email=email
        self.facultyId=facultyId
        self.address=address
        self.mobileNo=mobileNo
        self.subjectsTeaching=subjectsTeaching
        self.salary=salary
        self.dateJoined=dateJoined
    def getFullName(self):
        print(self.firstName+" "+ self.lastName)
    def changeAddress(self, newAddress):
        self.address = newAddress
        print(f"Address changed, new address is : {self.address}")
    def changeNumber(self, newNumber):
        self.mobileNo= newNumber
        print(f"Mobile number changes, new mobile number is : {self.mobileNo}")
    def getSalary(self):
        print(f"Your salary is {self.salary}")

class Student:
    def __init__(self, firstName, lastName, email, studentId, address, mobileNo, subjectsLearning, GPA, dateJoined):
        self.firstName=firstName
        self.lastName=lastName
        self.email=email
        self.studentId=studentId
        self.address=address
        self.mobileNo=mobileNo
        self.subjectsLearning=subjectsLearning
        self.GPA=GPA
        self.dateJoined=dateJoined
    def getFullName(self):
        print(self.firstName+" "+ self.lastName)
    def changeAddress(self, newAddress):
        self.address = newAddress
        print(f"Address changed, new address is : {self.address}")
    def changeNumber(self, newNumber):
        self.mobileNo= newNumber
        print(f"Mobile number changes, new mobile number is : {self.mobileNo}")
    def getGPA(self):
        print(f"Your GPA is: {self.GPA}")
