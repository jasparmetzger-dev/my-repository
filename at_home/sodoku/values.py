def man_eing ():
        val = [] 
        for i in range(81):
            val[i] = int(input(f"What will the value to the key {feld(i)} be? "))
            return val
    def aut_eing():
        return
    def start():
        autorman = input("Was the value input manually done?").lower
        values = None
    
        if autorman == 'yes': values = man_eing()
        elif autorman == 'no': values = aut_eing()
        keys = brett()
        start_dict = {}
        for i in range(81):
            start_dict[keys[i]] = values[i]
    
    #upload
    print(start())

    
    
