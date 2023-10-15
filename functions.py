from datetime import datetime
import PySimpleGUI as Sg


def edit(datainput):
    layout = [[Sg.InputText(default_text=datainput, do_not_clear=False, font=10, size=50, key="edit")],
              [Sg.Button(button_text="Ok"), Sg.Button(button_text="Cancel")]]
    window2 = Sg.Window(title="Edit window", layout=layout)
    while True:
        event, values = window2.read()
        match event:
            case "Cancel":
                break
            case "Ok":
                window2.close()
                return values['edit']


def read():
    try:
        with open("data.tdo", 'r') as store_file:
            countries = store_file.readlines()

    except FileNotFoundError:  # This is skipped if file exists
        with open('data.tdo', 'w') as store_file:
            pass
    return countries


wsad = read()


def write(data):
    with open('data.tdo', 'w') as store_file_def:
        store_file_def.writelines(data)


def pusta():
    print('Lista jest pusta !')


def data():
    datadzis = datetime.now().strftime("%d / %m / %y")
    return datadzis
