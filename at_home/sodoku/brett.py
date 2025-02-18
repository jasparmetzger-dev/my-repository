#brett mit namen
def brett():
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    sodoku = []
    for i in range(9):
        for letter in range(9):
            sodoku.append(str(i) + letters[letter])
    return sodoku

def feld(fe):
    br = brett()
    return br[int(fe)]

print(feld(12))