from functions import *
countries_done = []


while True:

    try:
        with open("data.tdo", 'r') as store_file:
            countries = store_file.readlines()

    except FileNotFoundError:  # This is skipped if file exists
        with open('data.tdo', 'w') as store_file:
            pass
    else:
        break


while True:
    print('Co chcesz zrobić?  ')
    print('---------------')
    print("1. Dodaj do listy")
    print("2. Zaznacz jako zakończone")
    print("3. Wyświetl listę")
    print("4. Edytuj wpis")
    print("5. Wyjdź")
    print("---------------")
    print('\n')
    usr = input("Podaj:")

# Dodaj
    if '1' in usr[0]:
        usr_input = usr.strip('1 ')
        if len(usr_input) > 1:
            countries.append(data() + " " + usr_input + '\n')
            write(countries)
        else:
            print('Nic do dodania')

# Zaznacz jako zakończone
    elif '2' in usr[0]:
        try:
            if len(countries) > 0:
                countries_done.append(countries.pop(int(input("Który element chcesz zaznaczyć jako ukończony?:"))-1))
                write(countries)

            else:
                pusta()
        except ValueError:
            print('Nie podałeś prawidłowej wartości.')
# Wyświetl listę
    elif '3' in usr[0]:
        read()
        if len(countries) > 0:
            for index, x in enumerate(countries):
                print(f"{index+1}. {x.strip()}")
        else:
            pusta()

# Edytuj wpis
    elif '4' in usr[0]:
        if len(countries) > 0 and len(usr[2:]) > 0:
            usr = int(usr[2:])-1
            countries[usr] = data() + str(" " + input('Podaj nową wartość:\n') + '\n')
            write(countries)

        else:
            if len(usr[2:]) > 0:
                pusta()
            else:
                print('Nie podałeś który element do edycji')

# exit
    elif '5' in usr[0]:
        break
    else:
        print('Niepoprawny wybór')
