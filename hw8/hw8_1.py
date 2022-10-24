class Student:
    def __init__(self,firstName, lastName, groupNumber, age):
        self.firstName = firstName
        self.lastName = lastName
        self.groupNumber = groupNumber
        self.age = age

    def getFullName(self):
        print(f'Student : {self.firstName}, {self.lastName}')

    def getAge(self):
        print(f'Age : {self.age}')

    def getGroupNumberr(self):
        print(f'Group : {self.groupNumber}')

    def setNameAge(self, firstName, lastName, age ):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        print("data has been changed!")

    def setGroupNumber(self, groupNumber):
        self.groupNumber = groupNumber
        print("data has been changed!")

Student1 = Student("Vlad", "Blushch", 6, 19)
Student2 = Student("Victor", "Petrov", 8, 22)
Student3 = Student("Andrey", "Cheh", 1, 20)
Student4 = Student("Dasha", "Markevich", 3, 21)
Student5 = Student("Katya", "White", 99, 2200)

Student1.getFullName()
Student1.getAge()
Student1.getGroupNumberr()
Student1.setGroupNumber(0)
Student1.getGroupNumberr()
print("---------------------------------------")
Student2.getFullName()
Student2.getAge()
Student2.getGroupNumberr()
print("---------------------------------------")
Student3.getFullName()
Student3.getAge()
Student3.getGroupNumberr()
Student3.setNameAge("Vasya", "Chatov", 222)
Student3.getFullName()
Student3.getAge()
print("---------------------------------------")
Student4.getFullName()
Student4.getAge()
Student4.getGroupNumberr()
print("---------------------------------------")
Student5.getFullName()
Student5.getAge()
Student5.getGroupNumberr()

