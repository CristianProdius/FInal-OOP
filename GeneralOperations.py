from MenuText import print_general_op_text
from Commands import create_faculty, search_student, display_all_faculties, display_field_faculties
from CommitCommand import CommitCommand
from StatusCommand import StatusCommand

def general_operations():
    choice = ""

    while choice != "b":
        print_general_op_text()
        choice = input().strip()
        parts = choice.split("/")
        if choice.startswith("nf/"):
            create_faculty(parts)
        elif choice.startswith("ss/"):
            search_student(parts)
        elif choice == "df":
            display_all_faculties()
        elif choice.startswith("df/"):
            display_field_faculties(parts)
        elif parts[0] == "commit":
            command = CommitCommand()
            command.invoke()
        elif parts[0] == "status":
            command = StatusCommand()
            command.invoke()
        elif choice == "b":
            break
        else:
            print("Invalid choice. Do you want to try again? y/n")
            decision = input().strip().lower()
            if decision != "y":
                print("Going back")
                choice = "b"