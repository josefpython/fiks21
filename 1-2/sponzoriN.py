import os
from typing import OrderedDict

def here(filename):
    return(os.path.normpath(os.path.dirname(os.path.abspath(__file__)) + "/" + filename))

try:
    with open(here("input.txt"), "r") as f:
        rawLines = f.read().split("\n")
except FileNotFoundError:
    print("[!] Soubor se vstupem nebyl nalezen:/")
    raise SystemExit

instrukce = list(int(i) for i in rawLines[0].split(" "))

idZvire = rawLines[1:instrukce[0]+1]

idJmeno = {}

for radek in idZvire:
    id, jmeno = radek.split(" ")
    idJmeno[int(id)] = jmeno

sponzorZvirata = rawLines[instrukce[1]:]

sponzorZvirataDict = {}

for line in sponzorZvirata:

    jmeno, zvirata = line.split(" ")[:1],line.split(" ")[2:]
    sponzorZvirataDict[jmeno[0]] = zvirata

zvireSponzori = OrderedDict()

for id in range(instrukce[0]):
    zvireSponzori[id] = []

for jmeno, zvirata in sponzorZvirataDict.items():
   
    for zvire in zvirata:

        zvireSponzori[int(zvire)].append(jmeno)

def sort(toSort):
    
    srtd = OrderedDict()
    srtdKeys = sorted(toSort, key=lambda k: len(toSort[k]), reverse=True)

    for i in srtdKeys[::-1]:
        srtd[i] = toSort.get(i)

    return srtd

zvireSponzor = {}

zvireSponzoriSorted = sort(zvireSponzori)

for i in range(instrukce[0]):
    try:

        id, sponzori = list(zvireSponzoriSorted.items())[0]

        sponzorPick = sponzori[0]
        zvireSponzor[id] = sponzorPick

        for idx, sponzori in zvireSponzoriSorted.items():
            if sponzorPick in sponzori:
                zvireSponzoriSorted[idx].remove(sponzorPick)

        zvireSponzoriSorted.popitem(last=False)

    except IndexError:
        zvireSponzoriSorted.popitem(last=False)

    zvireSponzoriSorted = sort(zvireSponzoriSorted)    

vysledek = []
vysledekAbc = ""

if len(zvireSponzor) == instrukce[0]:
    vysledekAbc = vysledekAbc + "Ano\n"
else:
    vysledekAbc = vysledekAbc + "Ne\n"

for id, sponzor in zvireSponzor.items():
    vysledek.append(idJmeno.get(id) + "+++" + sponzor)

for v in sorted(vysledek):
    jmeno, sponzor = v.split("+++")
    vysledekAbc = vysledekAbc + jmeno + " " + sponzor + "\n"

with open(here("output.txt"), "w+") as f:
    f.write(vysledekAbc[:-1])
    print("[i] Výsledek vypsán do souboru output.txt")