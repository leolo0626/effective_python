from collections import defaultdict
from Student import Student
class GradeBook :
    def __init__(self):
        self._students = defaultdict(Student)

    def get_student(self, name):
        return self._students[name]