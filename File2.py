def add_courses(File, new_courses):
    with open(File, 'a') as file:
        for course in new_courses:
            file.write(course + '\n')

def print_all_courses(File):
    with open(File, 'r') as file:
        contents = file.read()
        print(contents)

if __name__ == "__main__":
    File = "TMU_Courses.txt"

    additional_courses = [
        "6. ME (In Collaboration with TCS ION)",
        "7. PH.D. Chemistry",
        "8. Ph.D. Mathematics",
        "9. B.A. - LL.B(Hons.)",
        "10. M.B.B.S(Bachelor of Medicine and Bachelor of Surgery)"
    ]
    add_courses(File, additional_courses)
    print_all_courses(File)