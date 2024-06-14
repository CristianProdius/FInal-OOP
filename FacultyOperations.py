from MenuText import print_faculty_op_text
from Commands import enroll_student, graduate_student, display_enrolled_students, display_graduated_students, check_belonging_to_faculty
from CommitCommand import CommitCommand
from StatusCommand import StatusCommand

def faculty_operations():
    choice = ""

    while choice != "b":
        print_faculty_op_text()
        choice = input().strip()
        parts = choice.split("/")
        if parts[0] == "ns":
            enroll_student(parts)
        elif parts[0] == "gs":
            graduate_student(parts)
        elif parts[0] == "ds":
            display_enrolled_students(parts)
        elif parts[0] == "dg":
            display_graduated_students(parts)
        elif parts[0] == "bf":
            check_belonging_to_faculty(parts)
        elif parts[0] == "commit":
            command = CommitCommand()
            command.invoke()
        elif parts[0] == "status":
            command = StatusCommand()
            command.invoke()
        elif parts[0] == "b":
            break
        else:
            print("Invalid choice. Do you want to try again? y/n")
            decision = input().strip().lower()
            if decision != "y":
                print("Going back")
                choice = "b"