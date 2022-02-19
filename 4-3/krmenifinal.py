from itertools import count
import sys
from collections import defaultdict
from treelib import Tree
import time

def makeTree(root, graph):
    tree = Tree()
    tree.create_node(root,root)
    g = graph

    q = []
    v = set()
    
    q.append(root)
    
    while q:
        c = q.pop(0)
        for child in g[c]:
            if not (child in v):
                tree.create_node(child, child, parent=c)
                q.append(child)
        v.add(c)
    return tree

def moveRoot(root, tree: Tree):
    givenTree = tree
    newTree = tree.remove_subtree(root)
    
    newTree.paste(root,givenTree)
    return newTree
    

with sys.stdin as f:

    file = open("output.txt","r+")
    file.truncate(0)
    file.close()

    rl = f.read().split("\n")
    g = [i.split(" ") for i in rl[1:int(rl[0].split(" ")[0])]]
    qe = [i.split(" ") for i in rl[int(rl[0].split(" ")[0]):]]

    graph = defaultdict(list)
    tree = Tree()

    for friends in g:
        f,t = [int(i) for i in friends]
        graph[t].append(f)
        graph[f].append(t)

    root = 1

    tree.create_node(root,root)
    g = graph

    q = []
    v = set()
    
    q.append(root)
    
    while q:
        c = q.pop(0)
        for child in g[c]:
            if not (child in v):
                tree.create_node(child, child, parent=c)
                q.append(child)
        v.add(c)

    for k in qe:

        exp = 0

        nds = [int(c) for c in k[1:]]
        amnt = int(k[0])

        for c in nds:
            exp += tree.depth(c)
        #EXP DONE ^^ prepare SFL vv
        
        if amnt == 1:
            res = str(exp)


        elif (amnt == 3 or amnt == 2):
            tbworl = defaultdict(int)
            #Tree But With Only Relevant Nodes
            for nodee in nds:
                for tray in tree.rsearch(nodee):
                    tbworl[tray] += 1
            ans = 0
            for k,v in tbworl.items():
                if v != amnt:
                    ans +=1
           
            res = str(exp-ans)


        else:

            st = time.time()

            tbworl = defaultdict(set)
            #Tree But With Only Relevant Nodes
            
            for nodee in nds:
                prev = None
                for tray in tree.rsearch(nodee):
                    if prev != None:
                        tbworl[prev].add(tray)
                        tbworl[tray].add(prev)
                    prev = tray
            # CORRECT ^^^
            ks = set(tbworl.keys())
            bestWeight = exp
            root = 1
            #t=makeTree(root,tbworl)
            while True:
                childChanged = False
                ar = set([g.identifier for g in tree.children(root)]).intersection(ks)
                try:
                    
                    for child in ar:
                        t = makeTree(child,tbworl)
                        xy=0
                        for n in nds:
                            xy+=t.depth(n)
                        if xy < bestWeight:
                            bestWeight = xy
                            root = child
                            childChanged = True
                        
                    if not childChanged:
                        break
                except:
                    break

            print(f"{time.time()-st}")
            res = str(exp-bestWeight)

        with open("output.txt", "a") as ft:
            ft.write("\n"+res)