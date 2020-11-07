import json


class Student(object):

    def __init__(self):
        """Constructor"""
        print("Enter the data of user")

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_middleName(self):
        return self.middleName

    def get_personalPhone(self):
        return self.personalPhone

    def get_phone(self):
        return self.phone

    def get_additionalInfo(self):
        return self.additionalInfo

    def set_name(self, name):
        self.name = name

    def set_surname(self, surname):
        self.surname = surname

    def set_middleName(self, middleName):
        self.middleName = middleName

    def set_personalPhone(self, personalPhone):
        self.personalPhone = personalPhone

    def set_phone(self, phone):
        self.phone = phone

    def set_additionalInfo(self, additionalInfo):
        self.additionalInfo = additionalInfo

    def setAllData(self):
        print('Name: ')
        self.set_name(input())

        print('Surname: ')
        self.set_surname(input())

        print('Middlename: ')
        self.set_middleName(input())

        print('Personal phone: ')
        self.set_personalPhone(input())

        print('Phone: ')
        self.set_phone(input())

        print('Additional info: ')
        self.set_additionalInfo(input())

    def getAllData(self):
        return print({"name": self.get_name(),
                      "surname": self.get_surname(),
                      "middleName": self.get_middleName(),
                      "personalPhone": self.get_personalPhone(),
                      "phone": self.get_phone(),
                      "additionalInfo": self.get_additionalInfo()
                      })
