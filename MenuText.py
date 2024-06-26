def print_menu_text():
    print("Welcome to TUM's student management system!")
    print("What do you want to do?")
    print("g - General operations")
    print("f - Faculty operations")
    print("s - Student operations")
    print("commit - Commit changes")
    print("status - Check status")
    print()
    print("q - Quit program")
    print()
    print("Your input: ", end='')

def print_student_op_text():
    print("Student operations")
    print("What do you want to do?")
    print()
    print("be - batch enroll students (add the students' information in the enroll.txt file)")
    print("bg/email_1/em1il_2/... - batch graduate students (add as many graduates as you want)")
    print("commit - Commit changes")
    print("status - Check status")
    print()
    print("b - Back")
    print()
    print("Your input: ", end='')

def print_general_op_text():
    print("General operations")
    print("What do you want to do?")
    print()
    print("nf/<faculty name>/<faculty abbreviation>/<field> - create faculty")
    print("ss/<student email> - search student and show faculty")
    print("df- display faculties")
    print("df/<field> - display all faculties of a field")
    print("commit - Commit changes")
    print("status - Check status")
    print()
    print("b - Back")
    print()
    print("Your input: ", end='')

def print_faculty_op_text():
    print("Faculty operations")
    print("What do you want to do?")
    print()
    print("ns/<faculty abbreviation>/<first name>/<last name>/<email>/<day>/<month>/<year> - enroll a new student")
    print("gs/<email> - graduate student")
    print("ds/<faculty abbreviation> - display only the enrolled students")
    print("dg/<faculty abbreviation> - display only the graduated students")
    print("bf/<faculty abbreviation>/<email> - check if a student belongs to faculty")
    print("commit - Commit changes")
    print("status - Check status")
    print()
    print("b - Back")
    print()
    print("Your input: ", end='')