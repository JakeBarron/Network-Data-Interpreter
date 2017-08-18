# GraphMetrics
#....................................................................
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
FileName = sys.argv[2]

print(nx.info(G))


print(G.node["Russian Federation"])

#betweeness centrality
RUS = 'Russian Federation'
USA = 'USA'
JAP = 'Japan'
GER = 'Germany'
WOR = 'World'
UKR = 'Ukraine'

countries = {RUS,USA,JAP,GER,WOR,UKR}

BC = nx.betweenness_centrality(G,normalized=True,weight='weight')
EC = nx.eigenvector_centrality_numpy(G,weight='weight')
ASPL = nx.average_shortest_path_length(G,weight='weight')



#write to csv
import csv
with open(sys.argv[2],'w',newline='') as csvfile:
	writer = csv.writer(csvfile, dialect='excel',delimiter=',')
	
	writer.writerow(["Node", "Betweenness Centrality"])
	for c in countries:
		writer.writerow([c,BC[c]])

	writer.writerow([])
		
	writer.writerow(["Node", "Eigenvector_centrality"])	
	for c in countries:
		writer.writerow([c,EC[c]])

	writer.writerow([])

	writer.writerow(["Average shortest path length"])
	writer.writerow([ASPL])