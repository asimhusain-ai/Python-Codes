class Student:
    def set_details(self, name, roll_number, grade):
        self.name = name
        self.roll_number = roll_number
        self.grade = grade

    def display_details(self):
        print("Student Details:")
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Grade:", self.grade)
student = Student()

name = input("Enter Name:- ")
roll_number = input("Enter Rollno:-  ")
grade = input("Enter Frade:- ")

student.set_details(name, roll_number, grade)
print("--------------------------------")
student.display_details()