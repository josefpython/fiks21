import numpy as np
import sys

class Flock:

    def __init__(self, nodes, vector) -> None:

        self.nodes = nodes # [[X,Y],[X,Y], ... ]
        self.vector = vector # (X,Y)
            
    def findBounds(self):
        _min = _max = None

        # ax + by + c = 0
        a,b = self.vector
        a,b = -b,a

        for x,y in self.nodes:

            x,y = int(x), int(y)
            c = -( a*x + b*y ) # c = - ax - by

            # for y = 0 (intercept with x axis) -> x = -c / a (or y axis)
            ai = -c/a if abs(b) < abs(a) else -c/b
            
            if _max != None:
                _max = max(_max, ai)
                _min = min(_min, ai)
            else:
                _max = _min = ai

        return [_min,_max]

def solveFromBounds(v):
    ans = count = 0
    axis = []
  
    for x,y in v:

        axis.append([x, "start"])
        axis.append([y, "stop"])
  
    axis = sorted(axis)
  
    for g in axis:
  
        if g[1] == "start":
            count += 1
        if g[1] == "stop":
            count -= 1
  
        ans = max(ans, count)
  
    return ans

with sys.stdin as f:

    raw = f.read()
    nflocks, xvec, yvec = raw.split("\n")[0].split(" ")
    rawLns = [i.split(" ")[1:] for i in raw.split("\n")[1:]]
    flocks = [np.array_split(h, len(h)/2) for h in rawLns]

    print(solveFromBounds([Flock(fl,[int(xvec),int(yvec)]).findBounds() for fl in flocks]))