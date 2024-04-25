from datetime import datetime
from OperationLogic import StudentRole

class Student:
    def __init__(self, first_name: str, last_name: str, email: str, enrollment_date: datetime, date_of_birth: datetime, student_role: StudentRole):
        if first_name is None:
            raise ValueError("firstName must not be null")
        if last_name is None:
            raise ValueError("lastName must not be null")
        if email is None:
            raise ValueError("email must not be null")
        if enrollment_date is None:
            raise ValueError("enrollmentDate must not be null")
        if date_of_birth is None:
            raise ValueError("dateFormat must not be null")
        if student_role is None:
            raise ValueError("studentRole must not be null")

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.enrollment_date = enrollment_date
        self.date_of_birth = date_of_birth
        self.student_role = student_role

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def email(self):
        return self._email

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @property
    def enrollment_date(self):
        return self._enrollment_date

    @property
    def student_role(self):
        return self._student_role

    @student_role.setter
    def student_role(self, role):
        self._student_role = role