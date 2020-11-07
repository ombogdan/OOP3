import os, sys; sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from PhoneBook import PhoneBook

if __name__ == '__main__':
    phoneBook = PhoneBook()
    phoneBook.setAllData()
    # phoneBook.getAllData()

