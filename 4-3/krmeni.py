import sys
from collections import defaultdict
from treelib import Tree
import time

with sys.stdin as f:

    file = open("outputn.txt","r+")
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

        elif amnt == 3 or amnt == 2:
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

        elif amnt == 100:
            # [ [depth,[ pathToRoot ]], ... ]

            iterList = []

            st = time.time()

            tbworl = defaultdict(set)
            #Tree But With Only Relevant Nodes
            
            for nodee in nds:
                iterList.append([tree.depth(nodee),[]])
                pth = [x for x in tree.rsearch(nodee)][::-1][1:]
                iterList[-1][1] = pth

            print(f"{time.time()-st}")

            newBest = iterList
            bestd = exp
            changed = True
            while changed:
                changed = False
                bestList = newBest
                for i in bestList:
                    try:
                        chosen = i[1][0]
                    except:
                        pass
                    iLkeep = bestList
                    l = 0 
                    for x in iLkeep:
                        try:
                            if x[1][0] == chosen:
                                x[1].pop(0)
                                x[0] -= 1
                            else:
                                x[1].insert(0,chosen)
                                x[0] += 1
                            #print(iLkeep)
                        except:
                            x[1].insert(0,chosen)
                            x[0] += 1
                        
                    d = sum([a[0] for a in iLkeep])
                    if bestd > d:
                        changed = True
                        newBest = iLkeep
                        bestd = d

            res = str(exp-bestd)

        elif amnt == 50000:

            iterList = {}

            st = time.time()
            
            for nodee in nds:
                
                pth = [x for x in tree.rsearch(nodee)][::-1][1:]
                
                for d,p in enumerate(pth):
                    try:
                        iterList[d][p] += 1
                    except KeyError:
                        try:
                            iterList[d][p] = 1
                        except KeyError:
                            iterList.update({d:{p:1}})

            keeper = 0
            maxnode = 1
           
            for d,i in iterList.items():
                arr = [a[1] for a in list(i.items())]
                ns = [a[0] for a in list(i.items())]
                if len(arr)==1:
                    pass
                v = max(arr)
                node = ns[arr.index(v)]
                arr.remove(v)
                s = sum(arr)
           
                #print(v,s)
                if v >= s:
                    keeper += v-s
                    maxnode = node
                else:
                    break

            ree = Tree()
            root = maxnode
            print(root)
            ree.create_node(root,root)
            g = graph

            q = []
            v = set()
            
            q.append(root)
            
            while q:
                c = q.pop(0)
                for child in g[c]:
                    if not (child in v):
                        ree.create_node(child, child, parent=c)
                        q.append(child)
                v.add(c)

            keeper = 0
            for i in nds:
                keeper += ree.depth(i)

            res = str(exp-keeper)
            #print(res)
            print(f"{time.time()-st}")
            
        with open("outputn.txt", "a") as ft:
            ft.write("\n"+res)