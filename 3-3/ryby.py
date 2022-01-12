import numpy as np
import time

class Flock:

    def __init__(self, nodes, vector) -> None:

        self.nodes = nodes # [[X,Y],[X,Y], ... ]
        self.vector = vector # [X,Y]
            
    def findBounds(self):
        _min = _max = None

        # ax + by + c = 0
        a,b = self.vector
        a,b = -b,a

        for node in self.nodes:
            x,y = int(node[0]), int(node[1])
            c = -( a*x + b*y ) # c = - ax - by

            # for y = 0 (intercept with x axis) -> x = -c / a (or y axis)
            if abs(a) < abs(b):
                ai = -c/a
            else:
                ai = -c/b

            if _max != None:
                if ai > _max:
                    _max = ai
                elif ai < _min:
                    _min = ai
            else:
                _max = _min = ai

        return [_min,_max]

def solveFromBounds(v):

    ans = i = 0
    grid = []
  
    for i in range(len(v)):
  
        grid.append([v[i][0], 'x'])
        grid.append([v[i][1], 'y'])
  
    grid = sorted(grid)
  
    for i in range(len(grid)):
  
        if (grid[i][1] == 'x'):
            i += 1
        elif (grid[i][1] == 'y'):
            i -= 1

        ans = max(ans, i)
  
    return ans

with open("input.txt") as f:

    raw = f.read()
    nflocks, xvec, yvec = raw.split("\n")[0].split(" ")
    rawLns = [i.split(" ")[1:] for i in raw.split("\n")[1:]]
    flocks = [np.array_split(h, len(h)/2) for h in rawLns]

    start = time.time()
    print(f"Maximálně můžeme navštívit {solveFromBounds([Flock(fl,[int(xvec),int(yvec)]).findBounds() for fl in flocks])} hejn")
    print(f"Vyřešeno v čase {round(time.time()-start,2)}s")