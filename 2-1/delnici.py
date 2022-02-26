import dijkstra as dg

def vypsat_seznam(array):
    "Udělá ze seznamu string oddělený novým řádkem"
    ret = ""
    for iter in array:
        ret = ret + iter + "\n"
    return ret[:-1]

vysledek = ""

#prep phase

raw = open("input.txt", "r", encoding="utf8", newline="\n").read().split("\n")
zadani_arr = []

zadaniZacatky = []

for row in range(len(raw)):
    if len(raw[row].split(" ")) == 1 and row != 0:
        try:
            int(raw[row])
            zadaniZacatky.append(row)
        except Exception:
            pass

for line in range(len(zadaniZacatky)):
    try:
        zadani_arr.append(raw[zadaniZacatky[line]:zadaniZacatky[line+1]])
    except Exception:
        zadani_arr.append(raw[zadaniZacatky[line]:-1])

zadanis = []

for n in range(len(zadani_arr)):
    if n%2==0:
        zadanis.append([zadani_arr[n],zadani_arr[n+1][:-1],zadani_arr[n+1][-1]])

#prep phase done => zadanis
len(zadanis)

ictr = 1
for zadani in zadanis:

    print(str(ictr)+"/"+str(len(zadanis)))
    ictr+=1

    pocet_jazyku = zadani[0][0]
    jazyky = zadani[0][1:]
    pocet_prekladu = int(zadani[1][0])
    preklady = zadani[1][1:]
    z, na = zadani[2].split(" ")

    graph = dg.Graph()

    for preklad in range(pocet_prekladu):
        
        wrk = preklady[preklad].split(" ")
        weight, nodes = wrk[1], wrk[2:]

        for node in nodes:

            werk = nodes
            for item in werk:

                if node != item:
                    graph.add_edge(node, item, int(weight))

    ln = dg.dijsktra(graph, z, na)
    if ln[0]:
        vysledek = vysledek + "To nas bude stat " + str(ln[2]) + ",-.\nPocet prekladu: " + str(len(ln[1])-1) + ".\n" + vypsat_seznam(ln[1]) + "\n"
    else:
        vysledek = vysledek + "Takove prekladatele nemame.\n"

with open("output.txt", "w+", encoding="utf8", newline="\n") as f:
    f.write(vysledek)