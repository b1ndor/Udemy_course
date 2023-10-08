from functions import *
from datetime import datetime
import PySimpleGUI as Sg

Sg.theme('DarkBlue')   # Add a touch of color
# All the stuff inside your window.
layout = [  [Sg.Text(datetime.now().strftime("%d / %m / %y"))],
            [Sg.Text('Enter todo in below field')],
            [Sg.InputText()],
            [Sg.Button('Add'), Sg.Button('Exit'), Sg.Button('Show')]]

# Create the Window
window = Sg.Window('ToDo List', layout)
# Event Loop to process "events" and get the "values" of the inputs

try:
    with open("data.tdo", 'r') as store_file:
        countries = store_file.readlines()

except FileNotFoundError:  # This is skipped if file exists
    with open('data.tdo', 'w') as store_file:
        pass

while True:
    event, values = window.read()
    if event == Sg.WIN_CLOSED or event == 'Exit': # if user closes window or clicks cancel
        break
    elif event == 'Show':
        countries = read()
        if len(countries) > 0:
            for index, x in enumerate(countries):
                print(f"{index + 1}  {x.strip()}")
        else:
            pusta()
    elif event == 'Add':
        countries.append((datetime.now().strftime("%d / %m / %y")+values[0]+"\n"))
        write(countries)

window.close()