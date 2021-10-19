filename = 'graph.json'

import json
import networkx as nx
import matplotlib.pyplot as plt
from random import choices

with open(filename, 'r') as fl:
    graph = json.load(fl)


g = nx.from_dict_of_dicts(graph, create_using=nx.DiGraph)

g.nodes



plt.rcParams["figure.figsize"] = (40,20)



pos = nx.spring_layout(g, k=0.1, iterations=100)


nx.draw_networkx(g, pos)
plt.show()

dijk_p = nx.dijkstra_path(g, '0', '29', weight= 'weight')


gg = {k: {e: w['weight'] for e,w in v.items()} for k,v in graph.items()}

nodes, weights = zip(*[(k, v) for k,v in gg['0'].items()])

pher_g = {k: {e: 1.0 for e,w in v.items()} for k,v in gg.items()}

def ant(node='0', goal='29'):
    path, nset = [], set()

    cost = 0

    while True:
        if node == goal:

            return path + [node]

        nodes, weights = zip(*[(k, v) for k, v in pher_g[node].items()])

        ch = choices(nodes, weights)[0]

        if ch not in nset:
            path.append(node)
            nset.add(node)
            node = ch
        else:
            return None

ant_paths = [ant()for i in range (50)]

choices(nodes, weights=weights,k=20)

path = 0

for i in range(len(dijk_p)-1):#after ants, see what cost was
    path += gg[dijk_p[i]][dijk_p[i+1]]


pher_n = 1

pher_n / path


for ap in ant_paths:

    path = 0

    for i in range(len(ap) - 1):
        path += gg[ap[i]][ap[i + 1]]

    pher_to_deposit = pher_n / path

    for i in range(len(ap) - 1):
        pher_g[ap[i]][ap[i + 1]] += pher_to_deposit


for k1 in pher_g.keys():
    for k2 in pher_g[k1].keys():
        pher_g[k1][k2] -= 0.5

print(ant_paths)

nx.draw_networkx(g, pos)
plt.show()



