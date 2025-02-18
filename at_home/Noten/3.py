import numpy as np

def calc_mdl(mdl: float, vok: float):

    out = mdl * 0.67 + vok * 0.33
    return out

def calc(mdl: float, schrftl: float, weights: float):

    note = mdl * (1 - weights) + schrftl * weights
    return note

def get_noten():

    inp1 = input("Mündliche Noten: ")
    if inp1:
        mdl = [int(i) for i in inp1.split()]
        mdl = float(np.mean(mdl))

    inp2 = input("Schriftliche Noten: ")
    if inp2:
        schrftl = [int(i) for i in  inp2.split()]
        schrftl = float(np.mean(schrftl))

        weights = 0.33 if len(inp2.split()) < 2 else 0.5

    inp3 = input("Vokabeltests Noten: ")
    if inp3:
        vok = [int(i) for i in  inp3.split()]
        vok = float(np.mean(vok))

    return [mdl if mdl else 0, schrftl if schrftl else 0, vok if vok else 0, weights if weights else 0]

def returnvalue():
    m, s, v, w = get_noten()

    #init mdl
    mdl = None
    if m != 0 and v != 0:
        mdl = calc_mdl(m, v)
    elif 0 == m: mdl = v
    else: mdl = m

    #init schrftl
    note = None
    if s:
        note = calc(mdl, s, w)
    else: note = mdl

    return note

print(returnvalue())