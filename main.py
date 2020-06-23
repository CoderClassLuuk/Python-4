#################
#Import modules #
import os       #
import time     #
import random   #
#################

EX = ".txt"
LIJSTEN = "lijsten" + EX
GOEDANTWOORDEN = ["Goedzo!", "Dubieus pronkstuk, maar vooruit.", "YOOOO LETS GO!", "Correct, mijnheer.", ":)", "Nice", "Epische zet, mijn gepigmenteerde medemens.", "Correct & cool.", "Ga zo door, makker!", "Top hoor, kameraad!", "G O E D", "Lekker sahbe", "Hard bro"]
FOUTANTWOORDEN = ["F", "Incorrect, mijnheer.", "Nop", "Nope", "Fout", "Volgende keer beter", "Potjandriedubbeltjes, je antwoord klopt niet!", "NOOOOOB!!!", "XD je bent echt slecht", "A dombo", "Ding-dang-dong, your answer is wrong!", "GAME OVER", "FOUUUTTTTT"]

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def kiesLijst():
    print("\n1 = nieuwe lijst")
    print("2 = verwijder lijst")
    print("3 = overhoren")
    print("QQ = sluit programma")
    print("\nWil je terug gaan, gebruik dan altijd QQ.\n")

def nieuweLijst():
    newListInput = input("\nGeef je nieuwe lijst een naam (zonder extensie): ")
    lijstNaam = newListInput + EX
    with open(LIJSTEN, "a+") as file:
        file.write(lijstNaam + "\n")
    print("\nNieuwe lijst " + lijstNaam + " succesvol gemaakt.\n")
    clear()
    stopInLijst(lijstNaam)

def stopInLijst(lijstNaam):
    dicct = {}
    print("Typ eerst een key, daarna een value. Het eerste woord zal je moeten beantwoorden met de tweede.\n")
    print('Als je klaar bent met woorden toevoegen aan je lijst, typ dan "QQ"\n')
    print("Bijvoorbeeld: eerst Fiets, dan Bicycle.\n")
    lijstKey = input(": ")
    lijstValue = input(": ")
    while not (lijstKey.upper() == "QQ" or lijstValue.upper() == "QQ"):
        with open(lijstNaam, "a+") as file:
            file.write(lijstKey + ":" + lijstValue + "\n")
        dicct[lijstKey] = lijstValue
        print("Je hebt succesvol " + lijstKey + ":" + lijstValue + " in je lijst gezet.\n")
        lijstKey = input(": ")
        lijstValue = input(": ")
    clear()

def verwijderLijst():
    with open(LIJSTEN, "w+") as file:
        print("\nWelke lijst wil je verwijderen?")
        alleLijsten = file.read().split("\n")
        del alleLijsten[-1]
        print(alleLijsten)
        verwijderInput = input("Typ de naam van je lijst (met extensie): ")
        if verwijderInput in alleLijsten:
            print("\nLijst " + verwijderInput + " succesvol verwijderd.")
            os.remove(verwijderInput)
            verwijderLijn(verwijderInput, file)
        else:
            print("\nGebruik a.u.b een echte naam tho")
    clear()

def verwijderLijn(verwijderInput, f):
    lines = f.readlines()
    for line in lines:
        if line != verwijderInput + "\n":
            f.write(line)

def welkeLijst():
    print("\nOver welke lijst wil je overhoord worden?")
    with open(LIJSTEN, "r+") as file:
        alleLijsten = file.read().split("\n")
        del alleLijsten[-1]
    print(alleLijsten)
    overhoorInput = input("Typ de naam van je lijst (met extensie): ")
    overhoren(alleLijsten, overhoorInput)

def overhoren(alleLijsten, overhoorInput):
    goedCounter = 0
    foutCounter = 0
    while not overhoorInput.upper() == "QQ":
        if overhoorInput in alleLijsten:
            with open(overhoorInput, "r+") as file:
                overhoorLijst = file.read().split("\n")
                del overhoorLijst[-1]
                splitOnColon = []
                for i in overhoorLijst:
                    splitOnColon.append(i.split(":"))
                randomItem = random.randint(0, len(splitOnColon) - 1)
            overhoorQuestionInput = input(splitOnColon[randomItem][0] + " : ")
            if overhoorQuestionInput.upper() == "QQ":
                return
            if overhoorQuestionInput.upper() == splitOnColon[randomItem][1].upper():
                print(random.choice(GOEDANTWOORDEN))
                print("Het goede antwoord was: " + splitOnColon[randomItem][1])
                goedCounter = goedCounter + 1
                print("Aantal goede antwoorden: " + str(goedCounter))
                print("Aantal foute antwoorden: " + str(foutCounter) + "\n")
            else:
                print(random.choice(FOUTANTWOORDEN))
                foutCounter = foutCounter + 1
                print("Aantal goede antwoorden: " + str(goedCounter))
                print("Aantal foute antwoorden: " + str(foutCounter) + "\n")

        else:
            print("\nGebruik a.u.b een echte naam tho")
            return


def main():
    kiesLijst()
    userInput = input(": ")
    while not userInput.upper() == "QQ":
        if userInput == "1":
            nieuweLijst()
        elif userInput == "2":
            verwijderLijst()
        elif userInput == "3":
            welkeLijst()
        else:
            print("\nWat denk jij dat je doet, gekkerd?!")
        kiesLijst()
        userInput = input(": ")

main()