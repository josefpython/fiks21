import sys
from collections import defaultdict
import time

class World:
    def __init__(self) -> None:
        self.graph = defaultdict(list)
        self.paths = defaultdict(list)

    def addNodeAS(self, nodes):
        f,t = [int(i) for i in nodes]
        self.graph[t].append(f)
        self.graph[f].append(t)

    def helpMe(self):
        x=0
        for key,val in self.graph.items():
            if len(val) == 1:
                x+=1
                print(f"CUmslut bottom node::{key}")
                #print(self.retunShortestPath(key,1))
        return x


    def retunShortestPath(self, start, end):

        queue = [(start,[start])]
        visited = set()

        if start == end:
            return []

        while queue:
            vertex, path = queue.pop(0)
            visited.add(vertex)
            for node in self.graph[vertex]:
                if node == end:
                    return path + [end]
                else:
                    if node not in visited:
                        visited.add(node)
                        queue.append((node, path + [node]))

    def BFSthis(self, start, countries):
        res = 0

        countries = [int(c) for c in countries[1:]]

        visited = set()
        graph = self.graph #graph
        node = start #starting node
        queue = []

        depth = 0

        visited.add(node)
        queue.append(node)

        while queue:

            s = queue.pop(0) 

            depth+=1

            for neighbour in graph[s]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

                    if neighbour in countries:
                        res += depth
        return res

with sys.stdin as f:

    rl = f.read().split("\n")
    g = [i.split(" ") for i in rl[1:int(rl[0].split(" ")[0])]]
    q = [i.split(" ") for i in rl[int(rl[0].split(" ")[0]):]]

    s = World()
    for friends in g:
        s.addNodeAS(friends)
    #creates graph from input
    print("[i] created graph with " + str(len(s.graph))+" nodes, counting depths")
    print(s.helpMe())
    print("[i] idk something was done")

    startTime = time.time()

    for k in q:
        print("running k ")
        exp = s.BFSthis(1,k)
        sfl = exp
        for start in s.graph.keys():
            curr = s.BFSthis(start,k)
            if curr < sfl:
                sfl = curr

        res = str(exp-sfl)
        print(f"[!!! RESULT FOUND] ({res}) in {time.time()-startTime}s")
        with open("output.txt", "a") as ft:
            ft.write("\n"+res)