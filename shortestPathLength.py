import networkx as nx

G = nx.read_edgelist('edge_list.csv', create_using=nx.Graph(), delimiter=',', nodetype=str)

# sum is the sum of all shortest path length, count is used to find the average
sum1 = 0
count1 = 0
#shortest path length list containing shortest path of each node
spl = []

# calculate all shortest path length for all nodes
for node in G.nodes:
    G = nx.read_edgelist('edge_list.csv', create_using=nx.Graph(), delimiter=',', nodetype=str)
    G = nx.bfs_tree(G, node)
    shortest_path = nx.shortest_path_length(G)
    a, aDict = next(shortest_path)

    for key, value in aDict.items():
        sum1 = sum1 + value
        count1 = count1 + 1
    spl.append(sum1 / count1)

# calculate the average of the shortest path length
total = 0
average = 0
for i in spl:
    total = total + i
average = total / len(spl)
print(average)
