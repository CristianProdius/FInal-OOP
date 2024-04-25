import sys
from DataBase import FileManager
from Logging.Logger import Logger
from Templates import Faculty, Student, StudyField
from OperationLogic import UserInput, Storage

class GeneralOperations:
    logger = Logger()

    def start_operations(self):
        result = ""
        user_input = ""

        while result != "bk":
            user_input = input("G: Enter command:")
            result = self.do_operations(user_input)

    def do_operations(self, user_input):
        if len(user_input) < 2:
            print("String is too short!")
            return ""

        command_call = user_input[:2]
        command_operation = user_input[2:]

        if command_call == "nf":
            self.new_faculty(command_operation)
        elif command_call == "ss":
            self.search_student(command_operation)
        elif command_call == "df":
            self.display_faculties(command_operation)
        elif command_call == "br":
            FileManager.save_data()
            sys.exit(0)
        elif command_call == "bk":
            return "bk"
        elif command_call == "dh":
            self.display_help()
        else:
            print("No such command")

        return ""

    def new_faculty(self, command_operation):
        parts = command_operation.split("/")

        if len(parts) < 4:
            print("Incomplete command operation.")
            return

        faculty_name = parts[1]
        faculty_abbreviation = parts[2]
        try:
            study_field = StudyField[parts[3]]
        except KeyError:
            print("Invalid studyField")
            return

        Storage.add_faculty(Faculty(faculty_name, faculty_abbreviation, [], study_field))
        self.logger.log(f"Created faculty {faculty_abbreviation}")

    def search_student(self, command_operation):
        parts = command_operation.split("/")
        if len(parts) < 2:
            print("Incomplete command operation.")
            return

        student_email = parts[1]

        for faculty in Storage.get_all_faculties_list():
            for student in faculty.get_students():
                if student.get_email() == student_email:
                    print(f"Student is present in faculty: {faculty.get_name()}")
                    return

        print("Student is not present in any faculty")

    @staticmethod
    def display_faculties():
        for faculty in Storage.get_all_faculties_list():
            print(f"Name: {faculty.get_name()} | Abbreviation: {faculty.get_abbreviation()} | Field: {faculty.get_study_field()}")

    def display_faculties(self, command_operation):
        parts = command_operation.split("/")

        if len(parts) < 2:
            self.display_faculties()
            return

        try:
            study_field = StudyField[parts[1]]
        except KeyError:
            print("Invalid studyField")
            return

        for faculty in Storage.get_all_faculties_list():
            if faculty.get_study_field() == study_field:
                print(f"Name: {faculty.get_name()} | Abbreviation: {faculty.get_abbreviation()} | Field: {faculty.get_study_field()}")

    @staticmethod
    def display_help():
        print("""
        General operations

        nf/<faculty name>/<faculty abbreviation>/<field> - create (n)ew (f)aculty
        ss/<student email> - (s)earch (s)tudent and show faculty
        df - (d)isplay all (f)aculties
        df/<field> - (d)isplay all faculties of a (f)ield

        bk - back
        br - exit and save
        dh - (d)isplay (h)elp""")