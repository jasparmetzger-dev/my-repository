def calc(mdl, schrftl, vok):

        #mündlich
    mündlich = sum(mdl) / len(mdl)
    if vok != []:
        vokabeln = sum(vok) / len(vok)
        mündlich = mündlich * 0,67 + vokabeln * 0,33
        
    note = 0
    weights = 0,33 if len(schrftl) != 2 else 0,5
    if len(schrftl) == 0:
        note = mündlich
    else: 
        schriftlich = sum(schrftl) / len(schrftl)
        note = mündlich * (1 - weights) + schriftlich * weights
    return note

def findclass(name):
    with open("C:\\Users\\jaspa\\Desktop\\files\\Noten.txt", "r+") as f:
        lines = f.readlines()
        for i in lines: i.split(',')
        for i in range(len(lines)):
            if lines[i][0] == name:
                return lines[i]
        return None

def findline(name):
    with open("C:\\Users\\jaspa\\Desktop\\files\\Noten.txt", "r+") as f:
        lines = f.readlines()
        for i in lines: i.split(',')
        for i in range(len(lines)):
            if lines[i][0] == name:
                return i
        return None

def update(inp, line_to_change):
    with open("C:\\Users\\jaspa\\Desktop\\files\\Noten.txt", "r+") as f:
        lines = f.readlines()
    with open("C:\\Users\\jaspa\\Desktop\\files\\Noten.txt", "w") as f:
        for i in range(len(lines)):
            if i != line_to_change:
                f.write(lines[i])
        f.write(inp)

#notenstruct = ['Name', [ints schrftl noten], [mdl], [vok]]

type_of_inp = input('New Class(0), new grade(1) or calc grade(2)? ')

struct = [None, [], [], []]
new = None

if type_of_inp == '0':
    inp = input('New class: ').lower()
    new = struct
    new[0] = inp

    f = open("C:\\Users\\jaspa\\Desktop\\files\\Noten.txt", "a")
    f.write(str(new))
    f.close

elif type_of_inp == '1':
    print('Seperate with spaces:\n')
    inp = input('class, type of grade, grade').lower()
    inp = inp.split()
    #inp is a list

    class_ = findclass(inp[0])
    idx = None
    match inp[1]:
        case 'schrftl': idx = 1
        case 'mdl': idx = 2
        case 'vok': idx = 3
    class_[idx].append(inp[2])
    update(class_, findline(inp[0]))

elif type_of_inp == '2':
    inp = input('What class: ').lower()
    class_ = findclass(inp)
    grade = calc(class_[1], class_[2], class_[3])
    print(f"Your current grade in subject {inp} is {grade}")

else: print('Error 404')
