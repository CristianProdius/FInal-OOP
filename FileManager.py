import os
from pathlib import Path


DATA_FOLDER = os.path.join("")

STUDENT_FILE = os.path.join(DATA_FOLDER, "savedStudents.txt")
FACULTY_FILE = os.path.join(DATA_FOLDER, "savedFaculties.txt")
GRADUATE_FILE = os.path.join(DATA_FOLDER, "savedGraduates.txt")
ACTION_FILE = os.path.join(DATA_FOLDER, "actions.txt")
BATCH_ENROLL_FILE = os.path.join(DATA_FOLDER, "enroll.txt")

def save_data(command):
    data_to_save = command + "\n"
    if len(command) > 1:
        save_data_to_file(data_to_save, ACTION_FILE)
    if command.startswith("ns/"):
        save_data_to_file(data_to_save, STUDENT_FILE)
    elif command.startswith("nf/"):
        save_data_to_file(data_to_save, FACULTY_FILE)
    elif command.startswith("gs/"):
        save_data_to_file(data_to_save, GRADUATE_FILE)
    elif command.startswith("be/"):
        save_data_to_file(data_to_save, BATCH_ENROLL_FILE)
    elif command.startswith("bg/"):
        save_data_to_file(data_to_save, GRADUATE_FILE)

def load_data(file_name):
    data = []
    try:
        with open(file_name, 'r') as file:
            data = file.readlines()
    except IOError as e:
        print(e)
    return data

def load_student_data():
    return load_data(STUDENT_FILE)

def load_faculty_data():
    return load_data(FACULTY_FILE)

def load_graduate_data():
    return load_data(GRADUATE_FILE)

def load_batch_enroll_data():
    return load_data(BATCH_ENROLL_FILE)

def save_data_to_file(data, file_name):
    try:
        Path(DATA_FOLDER).mkdir(parents=True, exist_ok=True)
        with open(file_name, 'a') as file:
            file.write(data)
    except IOError as e:
        print(e)