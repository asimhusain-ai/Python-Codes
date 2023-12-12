class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print("Name: ",self.name)
        print("Age: ",self.age)

class Student(Person):
    def __init__(self, name, age, roll_number, grade):
        super().__init__(name, age)
        self.roll_number = roll_number
        self.grade = grade

    def display_student_details(self):
        self.display_details()
        print("Roll Number:- ",self.roll_number)
        print("Grade:- ",self.grade)

student1 = Student("Asim Husain", 19, "S12345", "A")
student1.display_student_details()