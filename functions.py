from datetime import datetime


def read():
    try:
        with open("data.tdo", 'r') as store_file:
            countries = store_file.readlines()

    except FileNotFoundError:  # This is skipped if file exists
        with open('data.tdo', 'w') as store_file:
            pass
    return countries


def write(data):
    with open('data.tdo', 'w') as store_file_def:
        store_file_def.writelines(data)


def pusta():
    print('Lista jest pusta !')


def data():
    datadzis = datetime.now().strftime("%d / %m / %y")
    return datadzis
