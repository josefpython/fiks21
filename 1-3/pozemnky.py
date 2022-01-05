from responsivepathing import here

#prep phase
raw = open(here("input"), "r").read().split("\n")

zadani_arr = []
zadaniZacatky = []

amnt = int(raw.pop(0))

i = 0
for row in raw:
    if len(row.split(" ")) == 1:
        zadaniZacatky.append(i)
    i += 1

for iter in range(amnt):

    if iter+1 != len(zadaniZacatky):
        
        zadani_arr.append( raw[zadaniZacatky[iter]:zadaniZacatky[iter+1]] )
    else:
      
        zadani_arr.append( raw[zadaniZacatky[iter]:] )

vysledek = ""

for zadani in zadani_arr:
    print(zadani)
    msqr = 0
    for line in zadani[1:]:
        print(line)
        zvire, pocet, vymera = line.split(" ")
        msqr = msqr + (int(pocet)*int(vymera))

    vysledek = vysledek + str(msqr) + "\n"

with open(here("output"), "w") as f:
    f.write(vysledek)