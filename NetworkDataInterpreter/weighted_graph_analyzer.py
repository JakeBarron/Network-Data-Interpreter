import sys
import matplotlib.pyplot as plt
import networkx as nx
import matplotlib as mpl
import numpy as np
from scipy.stats import linregress
from collections import Counter

print(sys.argv[1])
print(sys.argv[2])
G = nx.read_graphml(sys.argv[1])

graphName = sys.argv[2]

print(nx.info(G))

#output = open(graphName,'w')


weighted_in_degs = {}
maximum = max(G.in_degree(weight=True).values())

for n in G.nodes():
		in_deg = G.in_degree(n, weight=True)/maximum
		if in_deg not in weighted_in_degs:
			weighted_in_degs[in_deg] = 0
		weighted_in_degs[in_deg] +=1
in_items = sorted(weighted_in_degs.items())

weighted_out_degs = {}
maximum = max(G.in_degree(weight=True).values())

for n in G.nodes():
		out_deg = G.out_degree(n, weight=True)/maximum
		if out_deg not in weighted_out_degs:
			weighted_out_degs[out_deg] = 0
		weighted_out_degs[out_deg] +=1
out_items = sorted(weighted_out_degs.items())


fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot([k for (k,v) in in_items], [v for (k,v) in in_items],color='r')
ax.plot([k for (k,v) in out_items], [v for (k,v) in out_items],color='b')

#ax.legend(['In-degree','out_degree'])

ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel('normalized weight')
ax.set_ylabel('k')
plt.title(graphName)


#fig.savefig("Weighted_Degree_Distribution" + graphName + ".png")

plt.show()
