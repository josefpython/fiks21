from math import floor

def solve(W, H, X, Y, T):
    base = (T+1)**2
    base -= (max(0,T-X)*(max(0,T-X)+1))//2 #LEFT
    base -= ((max(0,(X+T)-W+1))*(max(0,(X+T)-W+2)))//2 #RIGHT
    base -= ((max(0,(Y+T)-H+1))*(max(0,(Y+T)-H+2)))//2 #TOP
    base -= ((max(0,T-Y))*(max(0,T-Y+1)))//2 #BOTTOM

    inArr = [max(0,(T-X)-(H-Y)), max(0,(T-X)-Y-1), max(0,(((X+T)-W+1)-(H-Y))), max(0,(((X+T)-W+1)-Y-1))]
    #inArr = [TL, BL, TR, BR]

    print([i>0 for i in inArr])
    if not all([i>0 for i in inArr]):
        for t in inArr:

            trem = 0
            
            while True:
                if t == 1:
                    trem +=1
                    break
                if t == 0:
                    break
                trem += t
                t -= 2

            #print(trem)
            base += trem
    else:
        base = int((W*H)//2)

    print(base)
    return str("{0:.0f}".format(base)) + "\n"

with open("input.txt", "r") as f:
    zadani = f.read().split("\n")[1:]

for z in zadani:
    f = open("output.txt", "a")
    W,H,X,Y,T=[int(i) for i in z.split(" ")]
    f.write(solve(W,H,X,Y,T))
    f.close()