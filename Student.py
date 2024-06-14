class Student:
    students_list = []

    def __init__(self, first_name, last_name, email, day, month, year, faculty_abbreviation):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.day = day
        self.month = month
        self.year = year
        self.faculty_abbreviation = faculty_abbreviation
        self.is_graduated = False

    @classmethod
    def add_student(cls, student):
        cls.students_list.append(student)

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, day):
        self._day = day

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, month):
        self._month = month

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        self._year = year

    @property
    def faculty_abbreviation(self):
        return self._faculty_abbreviation

    @faculty_abbreviation.setter
    def faculty_abbreviation(self, faculty_abbreviation):
        self._faculty_abbreviation = faculty_abbreviation

    @property
    def is_graduated(self):
        return self._is_graduated

    @is_graduated.setter
    def is_graduated(self, is_graduated):
        self._is_graduated = is_graduated

    @classmethod
    def get_students_list(cls):
        return cls.students_list

    def link_with_faculty(self, faculty):
        faculty.add_student(self)

    def graduate(self):
        self.is_graduated = True