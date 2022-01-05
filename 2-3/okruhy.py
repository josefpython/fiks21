from collections import defaultdict, deque
import os

def here(filename): #pro lepší manipulaci se soubory
    return(os.path.normpath(os.path.dirname(os.path.abspath(__file__)) + "/" + filename))

class Solve: #řešení pomocí BFS
    
    def __init__(self, edges):
        
        self.graph = defaultdict(list)
        for a,b in edges:
            self.graph[a].append(b)

    def doesExist(self, _from, to):
        
        done = set()

        nodes = deque([_from])

        while nodes:
            
            v = nodes.popleft()
            if v == to:
                return True
            
            done.add(v)

            for vertice in self.graph[v]:
                if vertice not in done:
                    nodes.append(vertice)

        return False

def openExecWrite(inputFile, outputFile):

    with open(here(inputFile), "r") as f:
        lines = f.read().split("\n")

    m, n, o = [int(x) for x in lines[0].split(" ")]
    edgesTxt, questionsTxt = lines[1:n+1], lines[n+1:]

    edges = [edge.split(" ") for edge in edgesTxt]
    questions = [que.split(" ") for que in questionsTxt]
    
    paths = Solve(edges)

    with open(here(outputFile), "w+") as f:
        s = ""
        for _from, to in questions:
            if paths.doesExist(_from,to):
                s = s + "Cesta existuje\n"
            else:
                s = s + "Cesta neexistuje\n"

        f.write(s[:-1])

openExecWrite("input.txt", "output.txt")