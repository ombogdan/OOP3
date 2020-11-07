import json


def setCountRecord():
    print('Write count of new record: ')


class PhoneBook(object):
    phoneBookList = []

    def __init__(self):
        """Constructor"""
        self.countRecord = int(input())
        setCountRecord()

    def __del__(self):
        """Destructor"""
        print("Deleted")

    def setAllData(self):
        for i in range(self.countRecord):
            arr = {"id": i + 1}

            print('Name: ')
            arr["name"] = input()

            print('Surname: ')
            arr["surname"] = input()

            print('Middlename: ')
            arr["middlename"] = input()

            print('Personal phone: ')
            arr["personalPhone"] = input()

            print('Phone: ')
            arr["phone"] = input()

            print('Additional info: ')
            arr["additionalInfo"] = input()

            self.setPhoneBookList(arr)

    def setPhoneBookList(self, arr):
        self.phoneBookList.append(arr)

    def getAllDataInJson(self):
        print(json.dumps(self.phoneBookList))
