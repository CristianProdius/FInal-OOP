class Faculty:
    faculty_list = []

    def __init__(self, name, abbreviation, study_field):
        self._name = name
        self._abbreviation = abbreviation
        self._study_field = study_field
        self._students = []

    @classmethod
    def add_faculty(cls, faculty):
        cls.faculty_list.append(faculty)

    def add_student(self, student):
        self._students.append(student)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def abbreviation(self):
        return self._abbreviation

    @abbreviation.setter
    def abbreviation(self, value):
        self._abbreviation = value

    @property
    def students(self):
        return self._students

    @students.setter
    def students(self, students):
        self._students = students

    @property
    def study_field(self):
        return self._study_field

    @study_field.setter
    def study_field(self, value):
        self._study_field = value

    @classmethod
    def get_faculty_list(cls):
        return cls.faculty_list

    @staticmethod
    def find_faculty_by_abbreviation(faculties, abbreviation):
        for faculty in faculties:
            if faculty.abbreviation == abbreviation:
                return faculty
        return None