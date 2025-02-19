# University Management System with Course Credits

# Dictionary to store student details
students = {}

# Dictionary to store course details (name and credits)
courses = {}

# Dictionary to store grades
grades = {}

# Student Module
def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = int(input("Enter Student Age: "))
    students[student_id] = {"name": name, "age": age}
    print(f"Student {name} added successfully.")

def display_students():
    if not students:
        print("No students available.")
    else:
        print("\nStudent List:")
        for student_id, details in students.items():
            print(f"ID: {student_id}, Name: {details['name']}, Age: {details['age']}")

# Course Module
def add_course():
    course_code = input("Enter Course Code: ")
    course_name = input("Enter Course Name: ")
    course_credits = int(input("Enter Course Credits: "))
    courses[course_code] = {"name": course_name, "credits": course_credits}
    print(f"Course {course_name} with {course_credits} credits added successfully.")

def display_courses():
    if not courses:
        print("No courses available.")
    else:
        print("\nCourse List:")
        for course_code, details in courses.items():
            print(f"Code: {course_code}, Name: {details['name']}, Credits: {details['credits']}")

# Grades Module
def assign_grade():
    student_id = input("Enter Student ID: ")
    course_code = input("Enter Course Code: ")
    grade = input("Enter Grade (S, A, B, C, D, F): ").upper()
    if student_id not in students:
        print("Student ID not found.")
        return
    if course_code not in courses:
        print("Course Code not found.")
        return
    if student_id not in grades:
        grades[student_id] = {}
    grades[student_id][course_code] = grade
    print(f"Grade {grade} assigned to student {student_id} for course {course_code}.")

def calculate_gpa():
    student_id = input("Enter Student ID to calculate GPA: ")
    if student_id not in grades or not grades[student_id]:
        print(f"No grades available for student {student_id}.")
        return
    total_weighted_grades = 0
    total_credits = 0
    grade_mapping = {"S": 10.0, "A": 9.0, "B": 8.0, "C": 7.0, "D": 6.0, "E": 5.0, "F": 0.0}
    
    for course_code, grade in grades[student_id].items():
        course_credits = courses[course_code]["credits"]
        grade_value = grade_mapping.get(grade, 0.0)
        total_weighted_grades += grade_value * course_credits
        total_credits += course_credits

    if total_credits == 0:
        print("No credits found for the courses.")
        return

    gpa = total_weighted_grades / total_credits
    print(f"GPA for student {student_id}: {gpa:.2f}")

# Main Module
def main():
    while True:
        print("\nUniversity Management System")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Add Course")
        print("4. Display Courses")
        print("5. Assign Grade")
        print("6. Calculate GPA")
        print("7. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            add_course()
        elif choice == "4":
            display_courses()
        elif choice == "5":
            assign_grade()
        elif choice == "6":
            calculate_gpa()
        elif choice == "7":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
