from importlib.resources import path
import sys
from collections import defaultdict
from treelib import Tree
import time

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
            # {depth:{node:amnt}, ..}

            iterList = {}

            st = time.time()

            tbworl = defaultdict(set)
            #Tree But With Only Relevant Nodes
            
            for nodee in nds:
                
                pth = [x for x in tree.rsearch(nodee)][::-1][:-1]
                
                for d,p in enumerate(pth):
                    try:
                        iterList[d][p] +=1 
                    except KeyError:
                        try:
                            iterList[d][p] = 1
                        except KeyError:
                            iterList.update({d:{p:1}})

            keeper = 0
            bestNode = 1

            for b,i in iterList.items():
            #iterate through every level
            #change to while loop so values can mutate I guess idk

                ch = False
                #change state to false

                for x in i.keys():
                    #iterate through every potential w

                    score = keeper
                   
                    for y in i.items():

                        if y[0] == x:
                            score -= y[1]
                        else:
                            score += y[1]
                    #count it up  for the dub n shit 

                    if score < keeper:
                        ch = True
                        keeper = score
                        bestNode = x
                
                if not ch:
                    break

            res = str(-keeper)
            print(f"{time.time()-st}")
            
        with open("output.txt", "a") as ft:
            ft.write("\n"+res)