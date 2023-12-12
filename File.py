def create_and_add_courses(File):
    with open(File, 'w') as file:
        file.write("TMU Courses:- \n")

    courses = [
        "1. BCA(Bachelor of Computer Applications)",
        "2. Ph.D. Computer Applications",
        "3. B.Tech (Specialization In Artificial Intelligence)",
        "4. B.Sc (Animation)",
        "5. Ph.d. Mechanical Engineering"
    ]

    with open(File, 'a') as file:
        for course in courses:
            file.write(course + '\n')

if __name__ == "__main__":
    File = "TMU_Courses.txt"
    create_and_add_courses(File)
    print("File ", File,"Created and Courses Added Successfully\nRun Next Program To See All Added Courses")