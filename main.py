#################
#Import modules #
import os.path  #
import random   #
#################

EX = ".wrd"
GOEDANTWOORDEN = ["Goedzo!", "Dubieus pronkstuk, maar vooruit.", "YOOOO LETS GO!", "Correct, mijnheer.", ":)", "Nice", "Correct & cool.", "Ga zo door, makker!", "Top hoor, kameraad!", "G O E D", "Lekker sahbe", "Hard bro"]
FOUTANTWOORDEN = ["F", "Incorrect, mijnheer.", "Nop", "Nope", "Fout", "Volgende keer beter", "Potjandriedubbeltjes, je antwoord klopt niet!", "NOOOOOB!!!", "XD je bent echt slecht", "A dombo", "Ding-dang-dong, your answer is wrong!", "FOUUUTTTTT"]

def kiesLijst():
    print("\n1 = nieuwe lijst / aan lijst toevoegen")
    print("2 = verwijder lijst")
    print("3 = verwijder woorden uit lijst")
    print("4 = overhoren")
    print("5 = weergeef woorden in lijst")
    print("QQ = sluit programma")
    print("\nWil je terug gaan, gebruik dan altijd QQ.\n")

def nieuweLijst():
    print("\nBestaande lijsten:")
    print(getLijsten())
    newListInput = input("\nGeef je nieuwe lijst een naam (zonder extensie) of typ de naam van de lijst waaraan je wilt toevoegen: ")
    lijstNaam = newListInput + EX
    if os.path.exists(lijstNaam):
        print("\nEr wordt nu aan " + lijstNaam + " toegevoegd.")
    elif lijstNaam.upper() != "QQ.WRD":
        print("\nNieuwe lijst " + lijstNaam + " succesvol aangemaakt.")
    else:
        return
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

def getLijsten():
    files = os.listdir(os.getcwd())
    files_wrd = [i for i in files if i.endswith('.wrd')]
    return files_wrd

def verwijderLijst():
    print("\nWelke lijst wil je verwijderen?")
    print(getLijsten())
    alleLijsten = getLijsten()
    verwijderInput = input("\nTyp de naam van je lijst (zonder extensie): ")
    newVerwijderInput = verwijderInput + EX
    if (newVerwijderInput in alleLijsten):
        print("\nLijst " + newVerwijderInput + " wordt verwijderd.")
        os.remove(newVerwijderInput)
    else:
        print("\n" + newVerwijderInput + " is niet een bestaande lijst.")

def welkeLijstWoorden():
    print("\nUit welke lijst wil je woorden verwijderen?")
    print(getLijsten())
    alleLijsten = getLijsten()
    woordLijstInput = input("\nTyp de naam van je lijst (zonder extensie): ")
    newWoordLijstInput = woordLijstInput + EX
    count = 0
    if (newWoordLijstInput in alleLijsten):
        with open(newWoordLijstInput, 'r') as file:
            for line in file:
                count += 1
        file.close()
        if count == 0 or 1:
            print("\nEr kunnen geen woorden verwijderd worden uit een lijst met nul of maar één paar woorden.")
            return
        else:
            print("\nDeze woorden zijn in de lijst " + newWoordLijstInput + ":\n")
            with open (newWoordLijstInput, "r") as file:
                print(file.read())
            lijnInput = input("\nTyp de lijn die je uit het bestand wilt halen: ")
            if (lijnInput.upper() != "QQ"):
                woordenVerwijderen(newWoordLijstInput, lijnInput)
            else:
                return
    else:
        print("\nDe gegeven lijst naam is niet geldig.")
        return

def woordenVerwijderen(newWoordLijstInput, lijnInput):
    with open (newWoordLijstInput, "r+") as file:
        lines = file.readlines()
        file.seek(0)
        file.truncate()
        for line in lines:
            if line.strip("\n") != lijnInput:
                file.write(line)
    print("\nGeselecteerde lijn succesvol uit het bestaand gehaald.")

def welkeLijstOverhoren():
    print("\nOver welke lijst wil je overhoord worden?")
    print(getLijsten())
    overhoorInput = input("Typ de naam van je lijst (zonder extensie): ")
    newOverhoorInput = overhoorInput + EX
    alleLijsten = getLijsten()
    overhoren(alleLijsten, newOverhoorInput)

def overhoren(alleLijsten, newOverhoorInput):
    goedCounter = 0
    foutCounter = 0
    while not newOverhoorInput.upper() == "QQ":
        if newOverhoorInput in alleLijsten:
            with open(newOverhoorInput, "r+") as file:
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
            print("\nDe gegeven lijst naam is niet geldig.")
            return

def weergeefWoorden():
    print(getLijsten())
    gekozenLijst = input("\nVan welke lijst wil je de woorden zien? (zonder extensie): ")
    newGekozenLijst = gekozenLijst + EX
    alleLijsten = getLijsten()
    if (newGekozenLijst in alleLijsten):
        with open(newGekozenLijst, "r") as file:
            print("\nDe woorden in " + newGekozenLijst + " zijn:\n")
            print(file.read())
    else:
        print("\n" + newGekozenLijst + " is niet een geldige lijst.")
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
            welkeLijstWoorden()
        elif userInput == "4":
            welkeLijstOverhoren()
        elif userInput == "5":
            weergeefWoorden()
        else:
            print("\nDe gegeven input is niet geldig.")
        kiesLijst()
        userInput = input(": ")

main()