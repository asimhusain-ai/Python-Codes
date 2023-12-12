class PersonalDetails:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_personal_details(self):
        print("Name: - ",self.name)
        print("Age:- ",self.age)

class MarksDetails(PersonalDetails):
    def __init__(self, name, age, sub1, sub2):
        super().__init__(name, age)
        self.sub1 = sub1
        self.sub2 = sub2

    def display_marks_details(self):
        super().display_personal_details()
        print("Subject 1:- ",self.sub1)
        print("Subject 2:- ",self.sub2)

student1 = MarksDetails("Asim Husain", 18, 90, 85)
student1.display_marks_details()