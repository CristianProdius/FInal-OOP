from FileManager import load_batch_enroll_data, save_data
from Faculty import Faculty
from Student import Student
from StudyField import StudyField

students = Student.get_students_list()
faculties = Faculty.get_faculty_list()
batch_enroll_data = load_batch_enroll_data()

def enroll_student(parts):
    if len(parts) == 8:
        save_data("/".join(parts))
        faculty_abbreviation = parts[1]
        student_first_name = parts[2]
        student_last_name = parts[3]
        email = parts[4]
        birth_day = int(parts[5])
        birth_month = int(parts[6])
        birth_year = int(parts[7])
        faculty = Faculty.find_faculty_by_abbreviation(faculties, faculty_abbreviation)
        if faculty is not None:
            student = Student(student_first_name, student_last_name, email, birth_day, birth_month, birth_year, faculty_abbreviation)
            student.add_student(student)
            student.link_with_faculty(faculty)
            faculty.add_student(student)
            print("New student enrolled.")
        else:
            print(f"Faculty not found for abbreviation: '{faculty_abbreviation}'. Please try again")
    else:
        print("Invalid input for enrolling a student. Please follow the format and try again.")

def graduate_student(parts):
    if len(parts) == 2:
        save_data("/".join(parts))
        email = parts[1]
        for student in students:
            if student.email == email:  # change this line
                student.graduate()
                print(f"Student with email {email} has graduated.")
                return
        print(f"Student with email {email} not found.")
    else:
        print("Invalid input for graduating a student. Please follow the format and try again")




def display_enrolled_students(parts):
    if len(parts) == 2:
        faculty_abbreviation = parts[1]
        print(f"Enrolled students for faculty {faculty_abbreviation}:")
        for student in students:
            if student.faculty_abbreviation == faculty_abbreviation and not student.is_graduated:  # change this line
                print(f" - {student.email}")  # change this line
    else:
        print("Invalid input for displaying the students. Please follow the format and try again.")
    print("\n")

def display_graduated_students(parts):
    if len(parts) == 2:
        faculty_abbreviation = parts[1]
        print(f"Graduated students for faculty {faculty_abbreviation}:")
        for student in students:
            if student.faculty_abbreviation == faculty_abbreviation and student.is_graduated:  # change this line
                print(f" - {student.email}")  # change this line
    else:
        print("Invalid input for displaying the graduates. Please follow the format and try again.")
    print("\n")

def check_belonging_to_faculty(parts):
    if len(parts) == 3:
        faculty_abbreviation = parts[1]
        email = parts[2]
        for student in students:
            if student.email == email and student.faculty_abbreviation == faculty_abbreviation:  # change this line
                print(f"Student with email {email} belongs to faculty {faculty_abbreviation}")
                return
        print(f"Student with email {email} does not belong to faculty {faculty_abbreviation}")
    else:
        print("Invalid input for checking the belonging to the faculty. Please follow the format.")
    print("\n")

def create_faculty(parts):
    if len(parts) == 4:
        save_data("/".join(parts))
        faculty_name = parts[1]
        faculty_abbreviation = parts[2]
        study_field = StudyField(parts[3])
        faculty = Faculty(faculty_name, faculty_abbreviation, study_field)
        faculty.add_faculty(faculty)
        print("New Faculty created.")
    else:
        print("Invalid input for creating a faculty. Please follow the format and try again")
    print("\n")

def search_student(parts):
    if len(parts) == 2:
        email = parts[1]
        student_found = False
        for student in students:
            if student.email == email:  
                print("Student found:")
                print(student.first_name + " " + student.last_name)  
                print("Belongs to faculty: " + student.faculty_abbreviation)  
                student_found = True
                break
        if not student_found:
            print("Student with email " + email + " not found.")
    else:
        print("Invalid input for searching a student. Please follow the format and try again")
    print("\n")

def display_all_faculties():
    print("The available faculties:")
    for faculty in faculties:
        print(" - " + faculty.name)
    print("\n")

def display_field_faculties(parts):
    if len(parts) == 2:
        field = parts[1]
        if StudyField.validation(field):
            print("The faculties from the " + field + " field are:")
            for faculty in faculties:
                if faculty.study_field.name == field:  # change this line
                    print(" - " + faculty.name)  # change this line
        else:
            print("There does not exist such a field. Please introduce a valid field and try again")
    else:
        print("Invalid input for displaying the faculties. Please follow the format and try again.")
    print("\n")

def batch_enroll():
    for student_info in batch_enroll_data:
        b_enroll_parts = student_info.split("/")
        if len(b_enroll_parts) == 8:
            save_data(student_info)
            faculty_abbreviation = b_enroll_parts[1]
            student_first_name = b_enroll_parts[2]
            student_last_name = b_enroll_parts[3]
            email = b_enroll_parts[4]
            birth_day = int(b_enroll_parts[5])
            birth_month = int(b_enroll_parts[6])
            birth_year = int(b_enroll_parts[7])
            student = Student(student_first_name, student_last_name, email, birth_day, birth_month, birth_year, faculty_abbreviation)
            students.append(student)
        elif print("Invalid input for enrolling a student. Please follow the format and try again."):
            return

def batch_graduate(emails):
    for email in emails:
        save_data("gs/" + email)
        student_graduated = False
        for student in students:
            if student.email == email:  # change this line
                student.graduate()
                print("Student with email " + email + " has graduated.")
                student_graduated = True
        if not student_graduated:
            print("No student found with email: " + email)
    print("\n")
    print("\n")
