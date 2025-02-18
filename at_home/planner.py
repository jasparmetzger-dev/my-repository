import datetime 

#point based system tracking daily achievements
def points_inp():
    points_sleep = int(input("How many hours did you sleep today? "))
    inp_school = input("Did you go to schol today? " ).lower()
    points_school = 0
    match inp_school:
        case 'yes': points_school += 5
        case 'no' : points_school -= 5
    points_sports = int(input("How many times did you do a sporty activity today? ")) * 10
    points_reading = int(input("How many pages have you read today? ")) / 2
    points_socialmedia = int(input("How many minutes did you spend on social media today? ")) / 15
    inp_leetcode = input("Did you solve a leetcode problem today? ").lower()
    points_leetcode = 0
    if inp_leetcode == 'yes': points_leetcode += 10
    points_brilliant = int(input("How many brilliant problems did you solve today? "))
    inp_kcal = input("how many kcal did you eat today? ")
    points_kcal = 0
    if inp_kcal.isdigit() == True:
        points_kcal = (int(inp_kcal) - 3000) / 100
    else: points_kcal = -15

    points = points_kcal + points_brilliant + points_leetcode + points_school + points_reading + points_sleep + points_sports - points_socialmedia
    return str(int(points))

def weights_inp():
    inp_w = float(input("What did you weigh today? "))
    return str(inp_w) + " kg"

def earnings_inp():
    inp_s = float(input("How much Money did you make today? "))
    return str(inp_s) + ' €'

def main():
    date_today = datetime.date.today()
    pt = points_inp()
    #creates a csv input
    input_today = f"{pt},{weights_inp()},{earnings_inp()},{date_today}\n"
    #appends input

    with open("C:\\Users\\jaspa\\OneDrive\\Desktop\\files\\Tagebuch.csv", 'a+') as file:
        file.write(input_today)
    print(pt)

main()