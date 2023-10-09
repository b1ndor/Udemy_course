from functions import *
from datetime import datetime
import PySimpleGUI as Sg

Sg.theme('DarkBlue')
layout = [[Sg.Text(datetime.now().strftime("%d / %m / %y"), font=("13"))],
    [Sg.Text('Enter todo in below field', font=("bold, 13"))],
    [Sg.InputText(do_not_clear=False, font=("Bold, 13"))],
    [Sg.Button('Add', font=("Bold, 13")), Sg.Button('Exit', font=("Bold, 13")), Sg.Button('Show', font=("Bold, 13"))]]

# Create the Window
window = Sg.Window('ToDo List', layout)


# main body of program
while True:
    event, values = window.read()
    match event:
        case Sg.WIN_CLOSED | 'Exit':  # if user closes window or clicks cancel
            break
        case 'Show':
            countries = read()
            if len(countries) > 0:
                for index, x in enumerate(countries):
                    print(f"{index + 1}  {x.strip()}")
            else:
                pusta()
        case 'Add':
            countries = read()
            countries.append((datetime.now().strftime("%d / %m / %y") + "  "+values[0]+"\n"))
            write(countries)

window.close()
