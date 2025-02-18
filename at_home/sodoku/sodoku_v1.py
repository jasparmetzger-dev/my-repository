class start_pos:
    def brett(self):
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        sodoku = []
        for i in range(9):
            for letter in range(9):
                sodoku.append(str(i) + letters[letter])
        return sodoku
    def feld(self, fe):
        br = brett(self=)
        return br[int(fe)]
    
    def man_eing (self):
        val = [] 
        for i in range(81):
            val[i] = int(input(f"What will the value to the key {feld(i)} be? "))
            return val
    def aut_eing(self):
        return
    
    def start(self):
        autorman = input("Was the value input manually done?").lower
        values = None
    
        if autorman == 'yes': values = man_eing()
        elif autorman == 'no': values = aut_eing()
        keys = brett()
        start_dict = {}
        for i in range(81): start_dict[keys[i]] = values[i]
        