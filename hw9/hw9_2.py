import json
with open('data.json','r') as f:
    data = json.loads(f.read())

class NewStudent:
    def method(self):
        print(self.firstname, self.lastname,  self.age, self.city)

Student = type("Student", (NewStudent,), data)
new_student = Student()
new_student.method()
