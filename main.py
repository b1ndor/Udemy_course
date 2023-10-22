from functions import *
import PySimpleGUI as Sg


Sg.theme('DarkBlue')

firstrow = \
    [
            [Sg.Text(text='Enter todo in below field:', font=10)],
            [Sg.InputText(do_not_clear=False, font=10, size=50, key='Add_f'), Sg.Button(button_text='Add', font=10)],

        ]

secondrow = \
    [
        [Sg.Listbox(read(), font=13, size=(49, 16), expand_y=True, key="lista"),
            Sg.Button(button_text='Edit', font=10), Sg.Button(button_text='Complete', font=10, key='Compl')],
        Sg.Button(button_text='Exit', font=10)
    ]

mainframe = [[Sg.Text(data())], [[firstrow, secondrow]]]

# Create the Window
window = Sg.Window(title='ToDo List', layout=mainframe, icon='icon1.ico')


# main body of program
while True:

    event, values = window.read()
    match event:
        case Sg.WIN_CLOSED | 'Exit':
            break
        case 'Compl':
            compl = values['lista'][0]
            todos_stored = read()
            index_to_erase = todos_stored.index(compl)
            todos_stored.pop(index_to_erase)
            write(todos_stored)
            window['lista'].update(read())

        case 'Edit':
            if len(values['lista']) < 1:
                pusta()
            else:
                dozmiany = values['lista'][0]
                todos_stored = read()
                index_to_edit = todos_stored.index(dozmiany)
                new_todos = edit(dozmiany)
                todos_stored[index_to_edit] = new_todos
                write(todos_stored)
                window['lista'].update(read())

        case 'Add':
            if len(values['Add_f']) < 1:
                pusta_linia()
            else:
                todos = read()
                todos.append((data() + "  "+values['Add_f']+"\n"))
                write(todos)
                window['lista'].update(todos)

window.close()
