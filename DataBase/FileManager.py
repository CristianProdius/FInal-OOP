import pickle
from OperationLogic import Storage
from Templates import Faculty

class FileManager:

    @staticmethod
    def save_data():
        try:
            with open('data.ser', 'wb') as out:
                pickle.dump(Storage.get_all_faculties_list(), out)
        except Exception as e:
            print(e)

    @staticmethod
    def load_data():
        try:
            with open('data.ser', 'rb') as in_file:
                obj1 = pickle.load(in_file)
                if isinstance(obj1, list):
                    faculties = [Faculty(faculty) for faculty in obj1]
                    Storage.load_faculties(faculties)
        except (FileNotFoundError, IOError):
            print("Data Base is empty.")
        except Exception as e:
            print(e)