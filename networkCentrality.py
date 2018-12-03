import networkx as nx
import matplotlib.pyplot as plt

g = nx.read_edgelist('edge_list.csv', create_using=nx.Graph(), delimiter=',', nodetype=str)

# closeness centrality
closeness_centrality_dict = nx.closeness_centrality(g)

# sort the centrality
sortedCentrality = sorted(closeness_centrality_dict.items(), key=lambda d: d[1], reverse=True)

# display the node with the highest centrality
print("centric node: ", sortedCentrality[0])

# count number of nodes each traversal of depth 1
bfs_dict = {}
for i in range(1, 11):
    try:
    	# apply bfs starting from the centric node
        current_bfs_list = list(nx.bfs_edges(g, source='Lee', depth_limit=i))
        bfs_dict[i] = len(current_bfs_list)
    except:
        print('error')

# draw scatter plot
for key, value in bfs_dict.items():
    plt.scatter(int(key), int(value), color='blue')
plt.title('Network Centrality')
plt.ylabel('r(j)')
plt.xlabel('j')
plt.show()
