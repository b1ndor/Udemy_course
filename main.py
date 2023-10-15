from functions import *
import PySimpleGUI as Sg


Sg.theme('DarkBlue')

firstrow = \
    [
            [Sg.Text(text='Enter todo in below field:', font=10)],
            [Sg.InputText(do_not_clear=False, font=10, size=50), Sg.Button(button_text='Add', font=10)],

        ]

secondrow = \
    [
        [Sg.Listbox(read(), font=13, size=(49, 16), expand_y=True, key="lista"),
            Sg.Button(button_text='Edit', font=10)], Sg.Button(button_text='Exit', font=10)
    ]
mainframe = [[Sg.Text(data())], [[firstrow, secondrow]]]

# Create the Window
window = Sg.Window(title='ToDo List', layout=mainframe)


# main body of program
while True:

    event, values = window.read()
    match event:
        case Sg.WIN_CLOSED | 'Exit':
            break
        case 'Edit':
            dozmiany = values['lista']
            if len(dozmiany) < 1:
                pass
            else:
                pass
                # todos = edit(dozmiany)
                # write(todos)

        case 'Add':
            todos = read()
            todos.append((data() + "  "+values[0]+"\n"))
            write(todos)
            window['lista'].update(todos)

window.close()
