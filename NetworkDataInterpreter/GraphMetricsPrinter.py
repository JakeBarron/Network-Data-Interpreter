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
G = nx.read_graphml(sys.argv[1])

print(nx.info(G))

#print(G.node["Russian Federation"])

#betweeness centrality
RUS = 'Russian Federation'
USA = 'USA'
JAP = 'Japan'
GER = 'Germany'
WOR = 'World'
UKR = 'Ukraine'

countries = {RUS,USA,JAP,GER,WOR,UKR}

# BC = nx.betweenness_centrality(G,normalized=True,weight='weight')
# EC = nx.eigenvector_centrality_numpy(G,weight='weight')
# ASPL = nx.average_shortest_path_length(G,weight='weight')

# density = nx.density(G)

# print("density of ", sys.argv[1], " = ", density)

print(nx.info(G))