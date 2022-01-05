import os
import math
import numpy as np

NL = "0b1010" # \n in binary
SP = "0b100000" # space in bin

def here(filename):
    return(os.path.normpath(os.path.dirname(os.path.abspath(__file__)) + "/" + filename))

def binToInt(binArr):
    return int("".join([chr(int(i,2)) for i in binArr]))

def c(nr):
    return math.ceil(nr/4)

def fileToBinABeat(filename):

    with open(here(filename), "rb") as f:
        binarr = []

        for char in f.read():
            binarr.append(bin(char))

        T = binToInt(binarr[:binarr.index(NL)])

        binarr = binarr[len(str(T))+1:] #get rid of first line?

        testy = []

        for x in range(T):

            duh = binarr[:binarr.index(NL)]

            A = binToInt(duh[:binarr.index(SP)])
            B = binToInt(duh[binarr.index(SP)+1:])
            binarr = binarr[binarr.index(NL)+1:]

            z=[]

            for i in range(A):
                
                N = binToInt(binarr[:binarr.index(SP)])
                duh = binarr[binarr.index(SP)+1:c(N)+len(str(N))+1]

                binarr = binarr[c(N)+len(str(N))+2:]

                z.append([N,duh])

            testy.append([B,z])

        return testy

def toBase(testsInBinary):
    for e,i in enumerate(testsInBinary):
        for c,x in enumerate(i[1]):

            N = x[0]

            a = list("".join([format(int(i,2),"08b") for i in x[1]]))
            a = np.array(np.array_split(a,len(a)/2)).tolist()
            f=""
            for q in a:
                q = "".join(q)
                if q == "00":
                    f=f+"A"
                if q == "01":
                    f=f+"C"
                if q == "10":
                    f=f+"G"
                if q == "11":
                    f=f+"T"
            

            # input(str(testsInBinary[e][1][c]) + "->" + f[:N])
            testsInBinary[e][1][c] = f[:N]


    return testsInBinary

def udelejBaze(filename):
    return toBase(fileToBinABeat(filename))
