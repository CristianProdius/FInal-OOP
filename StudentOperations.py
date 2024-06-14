from MenuText import print_student_op_text
from Commands import batch_enroll, batch_graduate
from CommitCommand import CommitCommand
from StatusCommand import StatusCommand

def student_operations():
    choice = ""

    while choice != "b":
        print_student_op_text()
        choice = input().strip()
        parts = choice.split("/", 1)
        if parts[0] == "be":
            batch_enroll()
        elif parts[0] == "bg":
            batch_graduate(parts[1].split("/"))
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