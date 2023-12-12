class Personal:
    def __init__(self, name, age, course, Roll):
        self.name = name
        self.age = age 
        self.course = course
        self.Roll = Roll 
    def showPersonal(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Course: ",self.course)
        print("Roll: ",self.Roll)
class Marks:
    def __init__(self,sub1,sub2,sub3,sub4,sub5):
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
        self.sub4 = sub4
        self.sub5 = sub5
    def showMarks(self):
        print("Python Programming: ",self.sub1)
        print("Data Structures & Algorithm: ",self.sub2)
        print("Mathematics: ",self.sub3)
        print("Digital Electronics: ",self.sub4)
        print("Database Management: ",self.sub5)

class Student(Personal, Marks):
    def __init__(self,name,age,course,Roll,sub1,sub2,sub3,sub4,sub5):
        Personal.__init__(self,name,age,course,Roll)
        Marks.__init__(self,sub1,sub2,sub3,sub4,sub5)

    def DisplayDetails(self):
        self.showPersonal()
        self.showMarks()

student = Student("Asimov", 19,"B.Tech CS[AI ML DL]", 12, 99, 98, 97, 96, 95)
student.DisplayDetails()