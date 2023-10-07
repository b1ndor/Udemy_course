from datetime import datetime


def read():
    with open("data.tdo", 'r') as store_file_def:
        countries_def = store_file_def.readlines()
    return countries_def


def write(data):
    with open('data.tdo', 'w') as store_file_def:
        store_file_def.writelines(data)


def pusta():
    print('Lista jest pusta !')


def data():
    datadzis = datetime.now().strftime("%d / %m / %y")
    return datadzis
