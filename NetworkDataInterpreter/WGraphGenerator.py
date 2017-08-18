#Weighted graph generator

import sys
import matplotlib.pyplot as plt
import networkx as nx
import matplotlib as mpl

print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[3])

G=nx.DiGraph()

import csv
with open(sys.argv[1],'r') as csvfile:
	reader = csv.reader(csvfile, dialect='excel')
	reader.__next__()
	for row in reader:
		if str(row[0]) == sys.argv[3]:
			if row[6] == 1:
				G.add_edge(row[7],row[4],weight=row[11])
			else:
				G.add_edge(row[4],row[7],weight=row[11])

print("average degree connectivity", nx.average_degree_connectivity(G))
print("info: ", nx.info(G))
#print(nx.adjacency_matrix(G))

#nx.draw_networkx(G, node_size=10)
#plt.show()

nx.write_graphml(G, sys.argv[2])