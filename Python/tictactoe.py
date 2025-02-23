def ist_gewonnen(item, felder):
    if felder[0] == felder[4] == felder[8] == item or felder[2] == felder[4] == felder[6] == item:
        return True
    for n in range(3):
        if felder[n] == felder[3+n] == felder[6+n] == item or felder[3*n] == felder[3*n + 1] == felder[3*n + 2] == item:
            return True
    return False


felder = ['1','2','3','4','5','6','7','8','9']
used = []
my_feld = f' {felder[0]} | {felder[1]} | {felder[2]} \n' + '---|---|---' + f'\n {felder[3]} | {felder[4]} | {felder[5]} \n' + '---|---|---' + f'\n {felder[6]} | {felder[7]} | {felder[8]} '

print(my_feld)
unentschieden = False
zuege = 0
felder = [' '] * 9
while zuege < 9:

    inp_kreuz = input("Kreuz am Zug: Auf welches Feld möchtest dsu setzen? (1-9) ")
    try: felder[int(inp_kreuz) - 1] = '+'
    except ValueError:
        print('ValueError. Spiel abgebrochen')
        break

    if inp_kreuz in used:
        print("Error: Dieses Feld ist schon belegt. Spiel abgebrochen")
        break
    elif len(used) == 8:
        unentschieden = True
    else: used.append(inp_kreuz)

    print(f' {felder[0]} | {felder[1]} | {felder[2]} \n' + '---|---|---' + f'\n {felder[3]} | {felder[4]} | {felder[5]} \n' + '---|---|---' + f'\n {felder[6]} | {felder[7]} | {felder[8]} ')
    
    if unentschieden:
        print("Game over: Unentschieden")
        break
    
    zuege += 1
    if ist_gewonnen('+', felder):
        print("Kreuz hat gewonnen!")
        break

    inp_kreis = input("Kreis am Zug: Auf welches Feld möchtest dsu setzen? (1-9) ")

    try: felder[int(inp_kreis) - 1] = 'o'
    except ValueError:
        print('ValueError. Spiel abgebrochen')
        break

    if inp_kreis in used:
        print("Error: Dieses Feld ist schon belegt. Spiel abgebrochen")
        break
    else: used.append(inp_kreis)

    print(f' {felder[0]} | {felder[1]} | {felder[2]} \n' + '---|---|---' + f'\n {felder[3]} | {felder[4]} | {felder[5]} \n' + '---|---|---' + f'\n {felder[6]} | {felder[7]} | {felder[8]} ')

    zuege += 1

    if ist_gewonnen('o', felder):
        print("Kreis hat gewonnen!")
        break