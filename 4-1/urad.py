import sys
from cpu import Memory, Process, CPUSpecificError
#TODO ARITHMETICS ERRORS!!!!

def decodeFunction(ttbit):
    thingy = f'{ttbit:032b}'
    thingy = thingy[8:]
    value = thingy[:16]
    instruct = thingy[16:]
    return (instruct,int(value,base=2))

with sys.stdin as inpt:
    raw = inpt.read().split("\n")
    Q = int(raw.pop(0))
    zadaniarr = []
    for ech in range(Q):
        P = int(raw.pop(0))
        z = []
        for ln in range(P):
            z.append(raw.pop(0))
        zadaniarr.append(z)
    
    for zadani in zadaniarr:

        hlavniPamet = Memory()
        processes = []

        for process in zadani:

            zraw = [int(i) for i in process.split(" ")]
            offset = zraw.pop(0)
            n = zraw.pop(0)

            for x in range(n):
                hlavniPamet.write(offset+x,zraw[x])

            processes.append(Process(offset))

        for process in processes:
            for x in range(5000):
                input(str(decodeFunction(2151)))
