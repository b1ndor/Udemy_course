import zipfile as zp
import PySimpleGUI as Pg

teksta = 'Wybierz plik do archiwizacji'
tekstb = 'Wybierz miejsce zapisu'


Layout = \
    [[Pg.Text(teksta, auto_size_text=False, size=20), Pg.Input(s=30),
        Pg.FilesBrowse('Wybierz', change_submits=True)],
        [Pg.Text(tekstb, auto_size_text=False, size=20), Pg.Input(s=30),
            Pg.SaveAs('Wybierz', file_types=(('Zip file', "*.zip"),))],
        [Pg.Button('Wykonaj'), Pg.Exit("Wyjście"), Pg.Text('Udało się', key="-TEXT-", visible=False, text_color="Red", font="Bold, 18")]]

okno = Pg.Window('Zip creator', Layout)
while True:
    event, values = okno.read()
    match event:
        case 'Wykonaj':
            okno["-TEXT-"].update(visible=True)

        case Pg.WIN_CLOSED | "Wyjście":
            break


okno.close()
