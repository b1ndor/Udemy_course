from functions import *
from datetime import datetime
import PySimpleGUI as Sg


Sg.theme('DarkBlue')


column1 = [
        [Sg.Text(datetime.now().strftime("%d / %m / %y"), font=13)],
        [Sg.Text('Enter todo in below field:', font=13)],
        [Sg.InputText(do_not_clear=False, font=13), Sg.Button('Add', font=12)],
        [Sg.Button('Exit', font=12), Sg.Button('Edit', font=12)]
        ]
column2 = [
        [Sg.Listbox(read(), size=(20, 12), expand_y=True, key="lista")]
         ]

layout = [
        [
            Sg.Column(column1),
            Sg.VSeperator(),
            Sg.Column(column2)]
        ]

# Create the Window
window = Sg.Window('ToDo List', layout)


# main body of program
while True:

    event, values = window.read()
    match event:
        case Sg.WIN_CLOSED | 'Exit':  # if user closes window or clicks cancel
            break
        case 'Edit':
            pass
        case 'Add':
            countries = read()
            countries.append((datetime.now().strftime("%d / %m / %y") + "  "+values[0]+"\n"))
            write(countries)
            # window('lista').update[(countries)]
            Sg.Listbox.update(values[0])
window.close()
