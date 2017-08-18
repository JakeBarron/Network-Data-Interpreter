import sys
import matplotlib.pyplot as plt
import networkx as nx
import matplotlib as mpl
import numpy as np
from scipy.stats import linregress
from collections import Counter

print(sys.argv[1])
#print(sys.argv[2])
G = nx.read_graphml(sys.argv[1])

#graphName = sys.argv[2]

print(nx.info(G))

#output = open(graphName,'w')

# in_degs = {}
# for n in G.nodes():
# 		in_deg = G.in_degree(n)
# 		if in_deg not in in_degs:
# 			in_degs[in_deg] = 0
# 		in_degs[in_deg] +=1
# in_items = sorted(in_degs.items())


# out_degs = {}
# for n in G.nodes():
# 		out_deg = G.out_degree(n)
# 		if out_deg not in out_degs:
# 			out_degs[out_deg] = 0
# 		out_degs[out_deg] +=1
# out_items = sorted(out_degs.items())

# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.plot([k for (k,v) in in_items], [v for (k,v) in in_items],color='r')
# ax.plot([k for (k,v) in out_items], [v for (k,v) in out_items],color='b')

# ax.legend(['In-degree','out_degree'])

# ax.set_xscale('log')
# ax.set_yscale('log')
# plt.title(graphName)


# #fig.savefig("Degree_Distribution" + graphName + ".png")

# plt.show()
