import time as t

def oefening1():
    for i in range(10):
        print("Hello World")

def oefening2():
    for i in range(10):
        print(5 * (i + 1))

def oefening3():
    n = input("Hoe vaak wil je hello world printen? : ")
    if n.isdigit():
        for i in range(int(n)):
            print("Hello World")
    else:
        print("Dat is geen int, gekkie!")

def oefening4():
    e = input("Wat wil je printen? : ")
    h = input("Hoevaak wil je dat printen? : ")
    if h.isdigit():
        for i in range(int(h)):
            print(e)
    else:
        print("Doe is even normaal, spekkerd!")

def oefening5():
    dipp = input("Typ een w o o r d : ")
    sipp = list(dipp)
    for i in range(len(dipp)):
        print(sipp[i] * (i + 1))

def oefening6():
    quetsoquatlis = input("Typ een getal : ")
    knapperd = input("Typ nog een getal : ")
    pils = input("Sorry maar... nog een keer? : ")
    if quetsoquatlis.isdigit() and knapperd.isdigit() and pils.isdigit():
        karel = max(int(quetsoquatlis), int(knapperd), int(pils))
        print("Het grootste getal van de drie is " + str(karel) + ".")
    else:
        print("HALT!")

def oefening7():
    do_the_mechrio = input("Typ nog een keer een w o o r d : ")
    everybody_do_the_mechrio = list(do_the_mechrio)
    mechrio = ''.join(everybody_do_the_mechrio[::-1])
    print(mechrio)

def oefening8():
    litty = input("Typ een woord om te checken of een palindrome is: ")
    bib = list(litty)
    bab = ''.join(bib[::-1])
    if bab == litty:
        print("Het woord " + litty + " is een palindrome.")
    else:
        print("nop!")



oefening1()
t.sleep(0.5)
print("\n")
oefening2()
t.sleep(0.5)
print("\n")
oefening3()
t.sleep(0.5)
print("\n")
oefening4()
t.sleep(0.5)
print("\n")
oefening5()
t.sleep(0.5)
print("\n")
oefening6()
t.sleep(0.5)
print("\n")
oefening7()
t.sleep(0.5)
print("\n")
oefening8()

#de oefeningen met dictionaries heb ik al in een ander programma gedaan