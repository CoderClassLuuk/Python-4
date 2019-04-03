import os
import time
import random

program = True
ex = ".hakan"
ex2 = ".jurjen"
lijsten = "lijsten" + ex2
dicct = {}
with open(lijsten, "w") as file:
    pass
goedAntwoorden = ["Goedzo!", "Dubieus pronkstuk, maar vooruit.", "YOOOO LETS GO!", "Correct, mijnheer.", ":)", "Nice", "Epische zet, mijn gepigmenteerde medemens.", "Correct & cool.", "Ga zo door, makker!", "Top hoor, kameraad!", "G O E D", "Lekker sahbe", "Hard bro"]
foutAntwoorden = ["F", "Incorrect, mijnheer.", "Nop", "Nope", "Fout", "Volgende keer beter", "Potjandriedubbeltjes, je antwoord klopt niet!", "NOOOOOB!!!", "XD je bent echt slecht", "A dombo", "Ding-dang-dong, your answer is wrong!", "GAME OVER", "FOUUUTTTTT"]
goedCounter = 0
foutCounter = 0

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def kiesLijst():
    print("\n1 = nieuwe lijst")
    print("2 = verwijder lijst")
    print("3 = overhoren")
    print("4 = sluit programma")
    print("\nWil je terug gaan, gebruik dan altijd QQ.\n")

def nieuweLijst():
    time.sleep(0.5)
    global newListInput
    newListInput = input("\nGeef je nieuwe lijst een naam: ")
    global lijstNaam
    lijstNaam = newListInput + ex
    with open(lijsten, "a+") as file:
        file.write(lijstNaam + "\n")
        file.close()
    with open(lijstNaam, "w+") as file:
        print("\nNieuwe lijst " + lijstNaam + " succesvol gemaakt.\n")
        time.sleep(0.5)
        clear()
        print("Typ eerst een key, daarna een value. Het eerste woord zal je moeten beantwoorden met de tweede.\n")
        print('Als je klaar bent met woorden toevoegen aan je lijst, typ dan "QQ"\n')
        print("Bijvoorbeeld: eerst Fiets, dan Bicycle.\n")
        time.sleep(0.25)
        lijstKey = input(": ")
        lijstValue = input(": ")
        while not (lijstKey.upper() == "QQ" or lijstValue.upper() == "QQ"):
            file.write(lijstKey + ":" + lijstValue + "\n")
            dicct[lijstKey] = lijstValue
            time.sleep(0.25)
            print("Je hebt succesvol " + lijstKey + ":" + lijstValue + " in je lijst gezet.\n")
            time.sleep(0.25)
            lijstKey = input(": ")
            lijstValue = input(": ")
        clear()
        print(lijsten)
        time.sleep(2)

def verwijderLijst():
    global verwijderInput
    verwijderInput = ""
    time.sleep(0.5)
    with open(lijsten, "r+") as file:
        print("\nWelke lijst wil je verwijderen?")
        alleLijsten = file.read().split("\n")
        del alleLijsten[-1]
        print(alleLijsten)
        verwijderInput = input("Typ de naam van je lijst : ")
        if verwijderInput in alleLijsten:
            print("\nLijst " + verwijderInput + " succesvol verwijderd.")
            os.remove(verwijderInput)
            alleLijsten = file.read().split("\n")
            del alleLijsten[-1]
            verwijderLijn(verwijderInput)
        else:
            print("\nGebruik a.u.b een echte naam tho")
        file.close()
    time.sleep(0.5)
    clear()

def verwijderLijn(self):
    global verwijderInput
    f = open(lijsten, "r")
    lines = f.readlines()
    f.close()
    f = open(lijsten, "w")
    for line in lines:
        if line != verwijderInput + "\n":
            f.write(line)
    f.close()

def overhoren():
    global goedCounter
    global foutCounter
    print("\nOver welke lijst wil je overhoord worden?")
    with open(lijsten, "r+") as file:
        alleLijsten = file.read().split("\n")
        del alleLijsten[-1]
        file.close()
    print(alleLijsten)
    overhoorInput = input("Typ de naam van je lijst : ")
    while not overhoorInput.upper() == "QQ":
        if overhoorInput in alleLijsten:
            with open(overhoorInput, "r+") as file:
                overhoorLijst = file.read().split("\n")
                del overhoorLijst[-1]
                splitOnColon = []
                for i in overhoorLijst:
                    splitOnColon.append(i.split(":"))
                randomItem = random.randint(0, len(splitOnColon) - 1)
                overhoor1 = splitOnColon[randomItem][0]
                overhoor2 = splitOnColon[randomItem][1]
                file.close()
            overhoorQuestionInput = input(overhoor1 + " : ")
            if overhoorQuestionInput.upper() == "QQ":
                return
            if overhoorQuestionInput.upper() == overhoor2.upper():
                print(random.choice(goedAntwoorden))
                goedCounter = goedCounter + 1
                print("Aantal goede antwoorden: " + str(goedCounter))
                print("Aantal foute antwoorden: " + str(foutCounter))
            else:
                print(random.choice(foutAntwoorden))
                foutCounter = foutCounter + 1
                print("Aantal goede antwoorden: " + str(goedCounter))
                print("Aantal foute antwoorden: " + str(foutCounter))

        else:
            print("\nGebruik a.u.b een echte naam tho")
            return

def sluitProgramma():
    global program
    print("\nWelterusten...")
    time.sleep(1.8)
    clear()
    program = False

def main():
    global program
    program = True
    while program:
        kiesLijst()

        userInput = input(": ")

        if userInput == "1":
            nieuweLijst()

        elif userInput == "2":
            verwijderLijst()

        elif userInput == "3":
            overhoren()

        elif userInput == str("4") or userInput.upper() == "QQ":
            sluitProgramma()

        else:
            print("\nWat denkt jij dat je doet, gekkerd?!")
            return

while program:
    main()