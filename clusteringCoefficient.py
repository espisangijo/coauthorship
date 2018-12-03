import networkx as nx

g = nx.read_edgelist('edge_list.csv', create_using=nx.Graph(), delimiter=',', nodetype=str)

# clustering coefficient calculation
ccs = nx.clustering(g)

#average clustering coefficient calculation
avg_clust = sum(ccs.values()) / len(ccs)
print("average clustering coefficient = ", avg_clust)
