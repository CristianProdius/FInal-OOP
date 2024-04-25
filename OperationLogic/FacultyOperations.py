import sys
from datetime import datetime
from DataBase import FileManager
from Logging.Logger import Logger
from Templates import Faculty, Student
from OperationLogic.StudentRole import StudentRole
from OperationLogic.Storage import Storage


logger = Logger("FacultyLogs.log")

class FacultyOperations:
    def __init__(self):
        self.scanner = input

    def start_operations(self):
        result = ""
        while result != "bk":
            print("F: Enter command:")
            user_input = self.scanner()
            result = self.do_operations(user_input)

    def do_operations(self, user_input):
        if len(user_input) < 2:
            print("String is too short!")
            return ""

        command_call = user_input[:2]
        command_operation = user_input[2:]

        if command_call == "ns":
            self.new_student(command_operation)
        elif command_call == "gs":
            self.graduate_student(command_operation)
        elif command_call == "de":
            self.display_enrolled()
        elif command_call == "dg":
            self.display_graduated()
        elif command_call == "bf":
            self.belongs_to_faculty(command_operation)
        elif command_call == "br":
            FileManager.save_data()
            sys.exit(0)
        elif command_call == "bk":
            return "bk"
        elif command_call == "dh":
            self.display_help()
        elif command_call == "ms":
            self.mass_operations("newStudents", command_operation)
        elif command_call == "mg":
            self.mass_operations("graduateStudents", command_operation)
        else:
            print("No such command")

        return ""

    def new_student(self, command_operation):
        parts = command_operation.split("/")

        if len(parts) < 7:
            print("Incomplete command operation.")
            return

        faculty_abbreviation = parts[1]

        if not self.does_faculty_exist(faculty_abbreviation, Storage.get_all_faculties_list()):
            print("Faculty Does Not Exist")
            return

        first_name = parts[2]
        last_name = parts[3]
        email = parts[4]

        try:
            enrollment_date = datetime.strptime(parts[5], "%d-%m-%Y")
            date_of_birth = datetime.strptime(parts[6], "%d-%m-%Y")
        except ValueError:
            print("Error parsing date")
            return

        for faculty in Storage.get_all_faculties_list():
            if faculty_abbreviation == faculty.get_abbreviation():
                faculty.add_student(Student(first_name, last_name, email, enrollment_date, date_of_birth, StudentRole.NOT_GRADUATED))
                logger.log("New student: " + first_name + " " + last_name)
                return

    def graduate_student(self, command_operation):
        parts = command_operation.split("/")
        if len(parts) < 2:
            print("Incomplete command operation.")
            return

        student_email = parts[1]

        for faculty in Storage.get_all_faculties_list():
            for student in faculty.get_students():
                if student_email == student.get_email() and student.get_student_role() == StudentRole.NOT_GRADUATED:
                    student.set_student_role(StudentRole.GRADUATED)
                    logger.log(str(student) + " Has Been Graduated")
                    return

        print("Student is not enrolled")

    def display_enrolled(self):
        for faculty in Storage.get_all_faculties_list():
            print("Faculty: " + faculty.get_name())
            for student in faculty.get_students():
                if student.get_student_role() == StudentRole.NOT_GRADUATED:
                    print("FirstName: " + student.get_first_name() + " | LastName: " + student.get_last_name() + " | Email: " + student.get_email() + " | DateOfBirth: " + str(student.get_date_of_birth()) + " | EnrollmentDate: " + str(student.get_enrollment_date()))

    def display_graduated(self):
        for faculty in Storage.get_all_faculties_list():
            print("Faculty: " + faculty.get_name())
            for student in faculty.get_students():
                if student.get_student_role() == StudentRole.GRADUATED:
                    print("FirstName: " + student.get_first_name() + " | LastName: " + student.get_last_name() + " | Email: " + student.get_email() + " | DateOfBirth: " + str(student.get_date_of_birth()) + " | EnrollmentDate: " + str(student.get_enrollment_date()))

    def belongs_to_faculty(self, command_operation):
        parts = command_operation.split("/")
        if len(parts) < 3:
            print("Incomplete command operation.")
            return

        faculty_abbreviation = parts[1]
        student_email = parts[2]

        for faculty in Storage.get_all_faculties_list():
            if faculty.get_abbreviation() == faculty_abbreviation:
                for student in faculty.get_students():
                    if student.get_email() == student_email and student.get_student_role() == StudentRole.NOT_GRADUATED:
                        print("Student is present in faculty.")
                        return

        print("Student is not present in faculty.")

    @staticmethod
    def does_faculty_exist(abbreviation, faculties):
        for faculty in faculties:
            if abbreviation == faculty.get_abbreviation():
                return True
        return False

    def display_help(self):
        print("""
        Faculty operations

        ns/<faculty abbreviation>/<firstName>/<LastName>/<email>/<day>/<month>/<year>/<day>/<month>/<year> - create student
        gs/<email> - (g)raduate (s)tudent
        de/<faculty abbreviation> - (d)isplay enrolled (s)tudents
        dg/<faculty abbreviation> - (d)isplay (g)raduated students
        bf/<faculty abbreviation>/<email> - check if student (b)elongs to (f)aculty
        ms/<file path> - (m)ass add (s)tudents
        mg/<file path> - (m)ass (g)raduate students

        bk - (b)ac(k)
        br - exit and save
        dh - (d)isplay (h)elp""")

    def mass_operations(self, operation, command_operation):
        index = command_operation.index("/")
        file_path = command_operation[index + 1:]

        try:
            with open(file_path, 'r') as file:
                logger.log("Start Mass Operation: ")
                for line in file:
                    if operation == "newStudents":
                        self.new_student(line)
                    elif operation == "graduateStudents":
                        self.graduate_student(line)
                    else:
                        print("Invalid mass operation")
                logger.log("End Mass Operation: ")

        except IOError:
            print("File not found")