import time
from multiprocessing.dummy import Pool as ThreadPool
from collections import defaultdict
from treelib import Tree, Node
from functools import partial

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

def onethread(k, tree):
    exp = 0

    nds = [int(c) for c in k[1:]]
    amnt = int(k[0])

    for c in nds:
        exp += tree.depth(c)
    #EXP DONE ^^ prepare SFL vv
    st = time.time()

    pool = ThreadPool(12)

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
    ks = tbworl.keys()
    bestWeight = exp
    root = 1

    while True:
        childChanged = False
        ar = set([g.identifier for g in tree.children(root)]).intersection(ks)
        if len(ar) > 0:
            
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
        else:
            break

    print(f"{time.time()-st}")
    return str(exp-bestWeight)

def main(tree,qe):
    pool = ThreadPool(12)
    hunnids = qe[30000:-3]

    res = pool.map(partial(onethread, tree=tree),hunnids)
    return res