def All_At_Once(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content
def Line_By_Line(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines
def Line_By_Line_Using_Context_Manager(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            print(line.strip())
file_path = 'TMU_Courses.txt'
content = All_At_Once(file_path)
print("Entire File At Once:- ")
print(content)
print("\n")

lines = Line_By_Line(file_path)
print("Line By Line:- ")
for line in lines:
    print(line.strip())
print("\n")

print("Line By Line Using Context Manager:- ")
Line_By_Line_Using_Context_Manager(file_path)
print("\n")