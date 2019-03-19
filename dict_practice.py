import time as t

stopProgram = False

test = {"Epic": "Gamer", "Dabie": "Bab"}

def nieuwElement():
    index = input("\nWat wil je gebruiken als index/key?\n: ")
    t.sleep(0.75)
    value = input("Wat wil je gebruiken als waarde/value?\n: ")
    test[index] = value
    t.sleep(0.75)
    print("\nHier zijn alle keys in je dictionary:\n")
    for key in test:
        print(key)
    print("\n")

def verwijderElement():
    verwijder = input("\nWelk element wil je verwijderen? Typ de index van het element om het te verwijderen.\n: ")
    if verwijder in test:
        del test[verwijder]
        t.sleep(1)
        print("\nJe hebt succesvol het element van " + verwijder + " verwijdert.")
    else:
        print("Stop met deze ongein, gekkie!")

def elementenWeergeven():
    print("\nDit zijn de keys van alle elementen in je dictionary:\n")
    for key in test:
        print(key + "\n")

def valueZien():
    print("\nVan welke key wil je de value zien?")
    valueInput = input(": ")
    if valueInput in test:
        print("\nDe value van de key " + valueInput + " is " + test[valueInput] + ".\n")
    else:
        print("Stop toch is met deze ongein, schobbejak!")


def main():
    stopProgram = False
    while not stopProgram:
        print("Wat wil je doen?\n")
        print("1: Een nieuw element toevoegen aan de dictionary")
        print("2: Een element verwijderen van de dictionary")
        print("3: Alle keys weergeven")
        print("4: De value van een key zien\n")
        userInput = input(": ")
        if userInput == "1":
            nieuwElement()
        elif userInput == "2":
            verwijderElement()
        elif userInput == "3":
            elementenWeergeven()
        elif userInput == "4":
            valueZien()
        else:
            print("Sterf.")
            stopProgram = True

main()