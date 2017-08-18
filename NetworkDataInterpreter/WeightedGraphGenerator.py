import sys
import matplotlib.pyplot as plt
import networkx as nx
import matplotlib as mpl

G2013=nx.DiGraph()
G2014=nx.DiGraph()
G2015=nx.DiGraph()
G2016=nx.DiGraph()

import csv
with open('./Data/TN_RUS_Arms.csv','r') as csvfile:
	reader = csv.reader(csvfile, dialect='excel')
	reader.__next__()

	for row in reader:
		print(row[0])
		if row[0] == str(2013):
			if row[1] == 1:
				G2013.add_edge(row[7],row[4],weight=row[11])
			else:
				G2013.add_edge(row[4],row[7],weight=row[11])
		if row[0] == str(2014):
			if row[1] == 1:
				G2014.add_edge(row[7],row[4],weight=row[11])
			else:
				G2014.add_edge(row[4],row[7],weight=row[11])
		if row[0] == str(2015):
			if row[1] == 1:
				G2015.add_edge(row[7],row[4],weight=row[11])
			else:
				G2015.add_edge(row[4],row[7],weight=row[11])
		if row[0] == str(2016):
			if row[1] == 1:
				G2016.add_edge(row[7],row[4],weight=row[11])
			else:
				G2016.add_edge(row[4],row[7],weight=row[11])
	
	nx.write_graphml(G2013, "Arm2013.GRAPHML")
	nx.write_graphml(G2014, "Arm2014.GRAPHML")
	nx.write_graphml(G2015, "Arm2015.GRAPHML")
	nx.write_graphml(G2016, "Arm2016.GRAPHML")	
	
	print("info: ", nx.info(G2013))
	print("info: ", nx.info(G2014))
	print("info: ", nx.info(G2015))
	print("info: ", nx.info(G2016))



#print("average degree connectivity", nx.average_degree_connectivity(G))
#print(nx.adjacency_matrix(G))

#nx.draw_networkx(G, node_size=10)
#plt.show()
