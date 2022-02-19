from itertools import count
import sys
from collections import defaultdict
from treelib import Node, Tree
import time

class World:
    def __init__(self) -> None:
        self.graph = defaultdict(list)
        self.tree = Tree()
        self.subtree = Tree()
        self.subgraph = defaultdict(list)

    def addNodeAS(self, nodes):
        f,t = [int(i) for i in nodes]
        self.graph[t].append(f)
        self.graph[f].append(t)

    def makeTree(self, root):

        self.tree.create_node(root,root)
        g = self.graph

        q = []
        v = set()
        
        q.append(root)
        
        while q:
            c = q.pop(0)
            for child in g[c]:
                if not (child in v):
                    self.tree.create_node(child, child, parent=c)
                    q.append(child)
            v.add(c)

    def makeSmallTree(self, node):
        self.subtree.create_node(1,1)
        for x in node:
            branch = [n for n in self.tree.rsearch(x)][::-1][1:]
            try:
                self.subtree.create_node(branch[0],branch[0],1)
                self.subgraph[branch[0]].append(1)
                self.subgraph[1].append(branch[0])
            except Exception:
                pass
            for en, n in enumerate(branch):
                try:
                    self.subtree.create_node(branch[en+1],branch[en+1],n)
                    self.subgraph[branch[en+1]].append(n)
                    self.subgraph[n].append(branch[en+1])
                except Exception:
                    pass
        return True

    def prayers(self,countries):
        tree = self.subtree
        #graph
        while True:

            rootVal = self.BFSthis(tree.root, countries)
            chIds = [i.identifier for i in tree.children(tree.root)]
            chvals = {}
            for child in chIds:
                chvals[child] = self.BFSthis(child, countries)

            if all([ch>rootVal for ch in chvals.values()]):
                break

            newRoot = min(chvals, key=chvals.get)
            tree = tree.subtree(newRoot)

        return rootVal

    def thoughts(self, countries, sf):
        mini = sf
        print(countries)
        for node in self.subgraph.keys():
            l = self.BFSthis(node, countries)
            if l < mini:
                mini = l

        return mini
            
    def BFSthis(self, start, countries):
            res = 0

            visited = set()
            graph = self.subgraph #graph
            node = start #starting node
            queue = []

            depth = 0

            visited.add(node)
            queue.append(node)

            # if start in countries:
            #     countries.remove(start)

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

    file = open("output.txt","r+")
    file.truncate(0)
    file.close()

    rl = f.read().split("\n")
    g = [i.split(" ") for i in rl[1:int(rl[0].split(" ")[0])]]
    q = [i.split(" ") for i in rl[int(rl[0].split(" ")[0]):]]

    s = World()
    for friends in g:
        s.addNodeAS(friends)

    s.makeTree(root=1)

    for k in q:

        s.subtree = Tree()
        s.subgraph = defaultdict(list)

        exp = 0

        nds = [int(c) for c in k[1:]]
        amnt = int(k[0])

        for c in nds:
            exp += s.tree.depth(c)
        #EXP DONE ^^ prepare SFL vv
        
        if amnt == 1:
            res = str(exp)

        else:
            print(f"exp = {exp}")

            s.makeSmallTree(nds)
            sfl = s.thoughts(nds, exp)

            res = str(exp-sfl)

            print(f"[!!! RESULT FOUND] ({res})")

        with open("output.txt", "a") as ft:
            ft.write("\n"+res)