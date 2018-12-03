import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

g = nx.read_edgelist('edge_list.csv', create_using=nx.Graph(), delimiter=',', nodetype=str)
node_similarity_list = []
node_list = []

# check every e(ij) to calculate w(ij)
with open('edge_list.csv', 'r') as f:
    line_list = []
    number_of_edges = 0
    for line in f:
        number_of_edges = number_of_edges + 1
        line_list = line.split(',')
        line_list[0] = line_list[0].strip()
        line_list[1] = line_list[1].strip()
        # common neighbor is w(ij)
        node_similarity_list.append(tuple((line_list[0], line_list[1], len(sorted(nx.common_neighbors(g, line_list[0], line_list[1]))))))
node_similarity_list.sort(key=lambda x: x[2])
node_similarity_list.reverse()

node_similarity_dict = {}

# deletion of edge
while g.size() != 0:
    count = 0
    division = int(number_of_edges / 100)
    for i in range(0, 101):
        k = i * division
        for j in range(k, k + division):
            try:
                # batch edge removal
                g.remove_edge(node_similarity_list[j][0], node_similarity_list[j][1])
            except:
                break
        # refresh component size listxxw
        component_size_list = [len(c) for c in sorted(nx.connected_components(g), key=len, reverse=True)]
        node_similarity_dict[i] = component_size_list[0]

# plot points from dictionary individually
for key, value in node_similarity_dict.items():
    plt.scatter(int(key), int(value), color='blue')

plt.title('Node Similarity')
plt.xlabel('% of deleted edges')
plt.ylabel('size of largest connected component')
plt.xlim([0, 100])
plt.ylim([0, 5000])
plt.show()
