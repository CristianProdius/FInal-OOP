from Templates import Faculty

class Storage:
    all_faculties_list = []

    @staticmethod
    def get_all_faculties_list():
        return Storage.all_faculties_list

    @staticmethod
    def add_faculty(faculty):
        Storage.all_faculties_list.append(faculty)

    @staticmethod
    def load_faculties(faculties):
        Storage.all_faculties_list = faculties