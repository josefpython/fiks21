from responsivepathing import here
from collections import OrderedDict
from sys import getsizeof

vysledek = ""

#prep phase
raw = open(here("input"), "r").read().split("\n")
zadani_arr = []

zadaniZacatky = []

i = 0
for row in raw:
    if len(row.split(" ")) == 3:
        zadaniZacatky.append(i)
    i += 1

for iter in range(int(raw[0])):

    if iter+1 != len(zadaniZacatky):
        
        zadani_arr.append( raw[zadaniZacatky[iter]:zadaniZacatky[iter+1]] )
    else:
      
        zadani_arr.append( raw[zadaniZacatky[iter]:] )

zadanin = 0

for zadani in zadani_arr:

    zadanin += 1
    print(str(zadanin) + "/" + raw[0])
    
    breakdown = zadani.pop(0)
    p, z, n = breakdown.split(" ")

    n = int(n)

    print("thats " + z + " dependency inputs")

    dependencies = []

    for i in range(int(p)):
        dependencies.append([])
    
    for dependency in zadani:
        x,y = dependency.split(" ")      
        dependencies[int(x)].insert(0,int(y))

    #created dic of dependencies, check if possible
    
    if False:
        pass

    #TODO
    # 2slow
    # <3
    

    else:

        print("dependencies sorted, cutting..")

        cutHistory = []
        fuck = False

        cut = []

        for dep in dependencies[n]:
            cut.append(dep)

        deepCut = []
        deepCut.append(n)

        fallback = 0

        while cut != []:

            if not set(cut) in cutHistory:

                cut.reverse()
                cut = list(dict.fromkeys(cut))
                cut.reverse()

                deepCut = deepCut + cut
                newCut = []
                
                for number in cut:

                    try:

                        for value in dependencies[number]:
                            newCut.append(value)

                    except KeyError:
                        pass

                cutHistory.append(set(cut))
                cut = newCut

                deepCut.reverse()
                deepCut = list(dict.fromkeys(deepCut))
                deepCut.reverse()
                

            else:
                fuck = True
                break


        if not fuck:

            deepCut.reverse()
            xyx = list(dict.fromkeys(deepCut))

            vysledek = vysledek + "pujde to " + " ".join(str(u) for u in xyx) + "\n"
            print("resulted possible")

        else:

            vysledek = vysledek + "ajajaj" + "\n"
            print("resulted impossible")
        

    
with open(here("output"), "w") as f:
    f.write(vysledek[:-1])