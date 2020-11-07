import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from Student import Student

if __name__ == '__main__':
    student = Student()
    student.setAllData()
    student.getAllData()
