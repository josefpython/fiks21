import sys
from cpu import Memory, Process

# TODO: Fix arithmetic operations, via. line 101 in output.txt
# Build teleport
# Build bombs
# 😎

def decodeFunction(ttbit):
    thingy = f'{ttbit:032b}'
    thingy = thingy[8:]
    value = thingy[:16]
    instruct = thingy[16:]
    return (int(instruct,base=2),int(value,base=2))

with sys.stdin as inpt:

    file = open("output.txt","r+")
    file.truncate(0)
    file.close()

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


        for cycle in range(5000):
            for process in processes:
                process: Process
                if process.is_alive:
                    instruct, value = decodeFunction(hlavniPamet.read(process.PC))
                    #print(process.tray.queue)
                    if instruct == 0:
                        process.nop()
                    elif instruct == 1:
                        process.pc()
                    elif instruct == 2:
                        process.push(value)
                    elif instruct == 3:
                        process.pop()
                    elif instruct == 4:
                        process.swap()
                    elif instruct == 5:
                        process.dup()
                    elif instruct == 6:
                        process.pushsize()
                    elif instruct == 7:
                        process.load(hlavniPamet)
                    elif instruct == 8:
                        try:
                            a,v = process.store(hlavniPamet)
                            hlavniPamet.write(a,v)
                        except TypeError:
                            pass
                    elif instruct == 9:
                        process.add()
                    elif instruct == 10:
                        process.sub()
                    elif instruct == 11:
                        process.div()
                    elif instruct == 12:
                        process.pow()
                    elif instruct == 13:
                        process.brz(value)
                    elif instruct == 14:
                        process.br3(value) 
                    elif instruct == 15:
                        process.br7(value)
                    elif instruct == 16:
                        process.brge(value)
                    elif instruct == 17:
                        process.jmp(value)
                    else:
                        process.is_alive = False

        answr = hlavniPamet.read(42)
        somepointrs = sum([(i.PC)%256 for i in processes])
        with open("output.txt", "a") as ft:
            ft.write(f"{answr} {somepointrs}\n")
        print(answr, somepointrs)