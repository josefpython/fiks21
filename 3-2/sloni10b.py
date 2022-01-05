from math import ceil
import time
def solve(W, H, X, Y, T):
    base = (T+1)**2
    base -= (max(0,T-X)*(max(0,T-X)+1))//2 #LEFT
    base -= ((max(0,(X+T)-W+1))*(max(0,(X+T)-W+2)))//2 #RIGHT
    base -= ((max(0,(Y+T)-H+1))*(max(0,(Y+T)-H+2)))//2 #TOP
    base -= ((max(0,T-Y))*(max(0,T-Y+1)))//2 #BOTTOM
    inArr = [max(0,(T-X)-(H-Y)), max(0,(T-X)-Y-1), max(0,(((X+T)-W+1)-(H-Y))), max(0,(((X+T)-W+1)-Y-1))]
    for t in inArr:
        if t%2 == 0:
            t = t//2
            base += (t*(t+1))
        else:
            t = (t-1)//2
            base += (t*(t+1))+t+1
    return str(round(base)) + "\n"

with open("input.txt", "r") as f:
    zadani = f.read().split("\n")[1:]

start = time.time()

for z in zadani:
    try:
        f = open("output.txt", "a")
        W,H,X,Y,T=[int(i) for i in z.split(" ")]
        f.write(solve(W,H,X,Y,T))
        f.close()
    except ValueError:
        pass

print("Alg. finished in " + str(round(time.time()-start,4))+" s")