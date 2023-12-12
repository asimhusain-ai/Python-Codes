student_names = []
while True:
    name = input("Enter a student's name (or press Enter to finish): ")
    if name:
        student_names.append(name)
    else:
        break
student_names.sort()
print("Sorted list of student names:")
for name in student_names:
    print(name)
