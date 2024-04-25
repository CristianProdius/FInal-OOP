from typing import List

class Faculty:
    def __init__(self, name: str, abbreviation: str, students: List['Student'], study_field: 'StudyField'):
        if name is None:
            raise ValueError("name must not be null")
        if abbreviation is None:
            raise ValueError("abbreviation must not be null")
        if students is None:
            raise ValueError("students must not be null")
        if study_field is None:
            raise ValueError("studyField must not be null")

        self.name = name
        self.abbreviation = abbreviation
        self.students = students
        self.study_field = study_field

    # Getter methods
    @property
    def name(self):
        return self._name

    @property
    def abbreviation(self):
        return self._abbreviation

    @property
    def students(self):
        return self._students

    @property
    def study_field(self):
        return self._study_field

    def add_student(self, student: 'Student'):
        self.students.append(student)

    def remove_student(self, student: 'Student'):
        self.students.remove(student)