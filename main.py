#################
#Import modules #
import os       #
import time     #
import random   #
#################

ex = ".txt"
lijsten = "lijsten" + ex
dicct = {}
with open(lijsten, "w") as file:
    pass
goedAntwoorden = ["Goedzo!", "Dubieus pronkstuk, maar vooruit.", "YOOOO LETS GO!", "Correct, mijnheer.", ":)", "Nice", "Epische zet, mijn gepigmenteerde medemens.", "Correct & cool.", "Ga zo door, makker!", "Top hoor, kameraad!", "G O E D", "Lekker sahbe", "Hard bro"]
foutAntwoorden = ["F", "Incorrect, mijnheer.", "Nop", "Nope", "Fout", "Volgende keer beter", "Potjandriedubbeltjes, je antwoord klopt niet!", "NOOOOOB!!!", "XD je bent echt slecht", "A dombo", "Ding-dang-dong, your answer is wrong!", "GAME OVER", "FOUUUTTTTT"]

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
    newListInput = input("\nGeef je nieuwe lijst een naam: ")
    lijstNaam = newListInput + ex
    # fname = "Users\LuukN\Desktop\CoderClassRobotica\Python\Python-4" + "\\" + lijstNaam
    with open(lijsten, "a+") as file:
        file.write(lijstNaam + "\n")
        file.close()
    print("\nNieuwe lijst " + lijstNaam + " succesvol gemaakt.\n")
    time.sleep(0.5)
    clear()
    return lijstNaam

def stopInLijst():
    lijstNaam = nieuweLijst()
    print("Typ eerst een key, daarna een value. Het eerste woord zal je moeten beantwoorden met de tweede.\n")
    print('Als je klaar bent met woorden toevoegen aan je lijst, typ dan "QQ"\n')
    print("Bijvoorbeeld: eerst Fiets, dan Bicycle.\n")
    time.sleep(0.25)
    lijstKey = input(": ")
    lijstValue = input(": ")
    while not (lijstKey.upper() == "QQ" or lijstValue.upper() == "QQ"):
        with open(lijstNaam, "w+") as file:
            file.write(lijstKey + ":" + lijstValue + "\n")
            file.close()
        dicct[lijstKey] = lijstValue
        time.sleep(0.25)
        print("Je hebt succesvol " + lijstKey + ":" + lijstValue + " in je lijst gezet.\n")
        time.sleep(0.25)
        lijstKey = input(": ")
        lijstValue = input(": ")
    clear()
    print(lijsten)
    time.sleep(2)

def verwijderLijst(verwijderInput):
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

def verwijderLijn(verwijderInput):
    f = open(lijsten, "r")
    lines = f.readlines()
    f.close()
    f = open(lijsten, "w")
    for line in lines:
        if line != verwijderInput + "\n":
            f.write(line)
    f.close()

def welkeLijst():
    print("\nOver welke lijst wil je overhoord worden?")
    with open(lijsten, "r+") as file:
        alleLijsten = file.read().split("\n")
        del alleLijsten[-1]
        file.close()
    print(alleLijsten)
    return alleLijsten

def overhoren(goedCounter, foutCounter):
    alleLijsten = welkeLijst()
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
    print("\nWelterusten...")
    time.sleep(1.8)
    clear()
    program = False
    return program

def main():
    program = True

    while program:
        kiesLijst()

        userInput = input(": ")

        if userInput == "1":
            stopInLijst()

        elif userInput == "2":
            verwijderLijst("")

        elif userInput == "3":
            overhoren(0, 0)

        elif userInput == "4" or userInput.upper() == "QQ":
             program = sluitProgramma()

        else:
            print("\nWat denkt jij dat je doet, gekkerd?!")
            return


main()