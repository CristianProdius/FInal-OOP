from DataBase import FileManager
from OperationLogic import FacultyOperations, GeneralOperations, UserInput

class MainApp:
    @staticmethod
    def main():
        print("dh - DisplaysHelp")
        FileManager.load_data()
        MainApp.main_menu()

    @staticmethod
    def main_menu():
        faculty_operations = FacultyOperations()
        general_operations = GeneralOperations()
        is_running = True
        while is_running:
            print("Enter something:")
            user_input = UserInput.scanner.readline().strip()

            if user_input == "f":
                faculty_operations.start_operations()
            elif user_input == "g":
                general_operations.start_operations()
            elif user_input == "br":
                FileManager.save_data()
                is_running = False
            elif user_input == "dh":
                MainApp.display_help()
            else:
                print("No such command")

    @staticmethod
    def display_help():
        print("""
        f - Go to Faculty Operations
        g - Go to General Operations

        dh - Display Help                        
        br - Exit and Save Program
        """)

if __name__ == "__main__":
    MainApp.main()