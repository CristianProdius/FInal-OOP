from FileManager import load_faculty_data, load_student_data, load_graduate_data
from Faculty import Faculty
from Student import Student
from StudyField import StudyField


students = Student.get_students_list()

def load_data():
    faculties_data = load_faculty_data()
    student_data = load_student_data()
    graduates_data = load_graduate_data()

    for faculty_info in faculties_data:
        parts = faculty_info.split("/")
        if len(parts) == 4:
            faculty_name = parts[1]
            faculty_abbreviation = parts[2]
            study_field = StudyField(parts[3].strip())
            faculty = Faculty(faculty_name, faculty_abbreviation, study_field)
            Faculty.add_faculty(faculty)

    for student_info in student_data:
        parts = student_info.split("/")
        if len(parts) == 8:
            faculty_abbreviation = parts[1]
            student_first_name = parts[2]
            student_last_name = parts[3]
            email = parts[4]
            birth_day = int(parts[5])
            birth_month = int(parts[6])
            birth_year = int(parts[7])
            student = Student(student_first_name, student_last_name, email, birth_day, birth_month, birth_year, faculty_abbreviation)
            students.append(student)



    for graduate_info in graduates_data:
        parts = graduate_info.split("/")
        if len(parts) == 2:
            email = parts[1]
            for student in students:
                if student.email == email:  
                    student.graduate()
                    break