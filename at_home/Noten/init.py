class noten:
    def __init__(self, name, mdl, schrtfl, vok):
        self.name = name
        self.mdl = mdl
        self.schrftl = schrtfl
        self.vok = vok

    def calc(self, mdl, schrftl, vok):
        #mündlich
        mündlich = sum(mdl) / len(mdl)
        if vok != []:
            vokabeln = sum(vok) / len(vok)
            mündlich = mündlich * 0,75 + vokabeln * 0,25
        
        note = 0
        weights = 0,33 if len(schrftl) != 2 else 0,5
        if len(schrftl) == 0:
            note = mündlich
        else: 
            schriftlich = sum(schrftl) / len(schrftl)
            note = mündlich * (1 - weights) + schriftlich * weights
        return note

def fach():
    lst = []
    physik = noten('physik', [], [], [])
    latein = noten('latein', [], [], [])
    mathe = noten('mathe', [], [], [])
    chemie = noten('chemie', [], [], [])
    philo = noten('philo', [], [], [])
    deutsch = noten('deutsch', [], [], [])
    seminarf = noten('seminarf', [], [], [])



fächer_dict = {
    'ph' : 0,
    'ma' : 1,
    'la' : 2,
    'ch' : 3,
    'pl' : 4,
    'de' : 5,
    'sf' : 6,
    'ge' : 7,
    'po' : 8,
    'if' : 9,
    'mu' : 10,
    'sp' : 11   
}

