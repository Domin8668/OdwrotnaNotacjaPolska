def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True

while True:
    menu = input('''1) Konwersja z notacji infiksowej do postfiksowej\n2) Konwersja z notacji postfiksowej do infiksowej\n3) Zakończenie programu\nWybierz w menu: ''')

    if menu == '1':
        print("Wciśnij spację i enter aby zakończyć wpisywanie.")
        stos = []
        wyjscie = []
        priorytet = {
            ')': 4,
            '^': 3,
            '*': 2,
            '/': 2,
            '+': 1,
            '-': 1,
            '(': 0
            }
        while True:
            symbol = str(input('\nPodaj symbol: '))
            if symbol == ' ':
                for i in range(len(stos)):
                    wyjscie.append(stos[-(1 + i)])
                print("Wyjście końcowe: ", wyjscie)
                wyjscie, stos = [], []
                break
                system('PAUSE')
            if len(symbol) != 1 and not is_number(symbol):
                print('Błąd. Podaj poprawny symbol.')
            else:
                if is_number(symbol):
                    wyjscie.append(symbol)
                    print("Wyjscie: ", wyjscie, "\nStos: ", stos)
                elif (ord(symbol) >= 42 and ord(symbol) <= 47 and symbol != ('.' or ',')) or symbol == '^':
                    if not len(stos):
                        stos.append(symbol)
                        print("Wyjscie: ", wyjscie, "\nStos: ", stos)
                    elif priorytet[stos[-1]] < priorytet[symbol]:
                        stos.append(symbol)
                        print("Wyjscie: ", wyjscie, "\nStos: ", stos)
                    elif priorytet[stos[-1]] >= priorytet[symbol]:
                        while priorytet[stos[-1]] >= priorytet[symbol]:
                            if stos[-1] != ('(' or ')'):
                                wyjscie.append(stos[-1])
                            stos.pop(-1)
                            print("Wyjscie: ", wyjscie, "\nStos: ", stos)
                            stos.append(symbol)
                        print("Wyjscie: ", wyjscie, "\nStos: ", stos)
                elif symbol == '(':
                    stos.append(symbol)
                    print("Wyjscie: ", wyjscie, "\nStos: ", stos)
                elif symbol == ')':
                    while stos[-1] != '(':
                        if stos[-1] != ('(' or ')'):
                            wyjscie.append(stos[-1])
                        stos.pop(-1)
                        print("Wyjscie: ", wyjscie, "\nStos: ", stos)
                    stos.pop(-1)
                    print("Wyjscie: ", wyjscie, "\nStos: ", stos)
                else: 
                    print('Błąd. Podaj poprawny symbol.')
    if menu == '2':
        print("\nWciśnij spację i enter aby zakończyć wpisywanie.")
        stos = []
        dzialanie = ''
        while True:
            symbol = str(input('\nPodaj symbol: '))
            if symbol == ' ':
                print("Stos końcowy: ", stos)
                stos = []
                dzialanie = ''
                break
                system('PAUSE')
            if len(symbol) != 1 and not is_number(symbol):
                print('Błąd. Podaj poprawny symbol.')
            else:
                if is_number(symbol):
                    stos.append(symbol)
                    print("Działanie: ", dzialanie, "\nStos: ", stos)
                elif (ord(symbol) >= 42 and ord(symbol) <= 47 and symbol != ('.' or ',')) or symbol == '^':
                    dzialanie = '(' + str(stos[-2]) + str(symbol) + str(stos[-1]) + ')'
                    stos.pop(-1)
                    stos.pop(-1)
                    stos.append(dzialanie)
                    print("Działanie: ", dzialanie, "\nStos: ", stos)
                    dzialanie = ''
                else:
                    print('Błąd. Podaj poprawny symbol.')
    if menu == '3':
        break
        system('PAUSE')
    else:
        print('Błąd. Podaj prawidłową liczbę.')