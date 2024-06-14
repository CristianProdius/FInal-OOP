import time
import threading
from FolderMonitor import FolderMonitor
from CommitCommand import CommitCommand
from StatusCommand import StatusCommand
from DataLoad import load_data
from GeneralOperations import general_operations 
from FacultyOperations import faculty_operations 
from StudentOperations import student_operations 
from MenuText import print_menu_text

def access_menu():
    load_data()

    next_command = ""

    file_monitor = FolderMonitor()
    threading.Thread(target=file_monitor.start_file_monitoring).start()

    while next_command != "q":
        print_menu_text()

        next_command = input().lower()
        parsed_command = parse_command(next_command)

        if parsed_command[0] == "commit":
            command = CommitCommand()
            command.invoke()
        elif parsed_command[0] == "status":
            command = StatusCommand()
            command.invoke()
        elif parsed_command[0] == "g":
            general_operations()
        elif parsed_command[0] == "f":
            faculty_operations()
        elif parsed_command[0] == "s":
            student_operations()
        elif parsed_command[0] == "q":
            print("Quiting the program")
            exit(0)
        else:
            print("Invalid choice. Do you want to try again? y/n")
            decision = input().strip().lower()
            if decision != "y":
                print("Quiting the program")
                next_command = "q"

        time.sleep(5)  # Sleep for 5 seconds

def parse_command(input):
    return input.split(" ")

if __name__ == "__main__":
    access_menu()