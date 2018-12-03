from networkx.algorithms import community
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

g = nx.read_edgelist('edge_list.csv', create_using=nx.Graph(), delimiter=',', nodetype=str)

# k-clique community detection algorithm
community_generator = community.k_clique_communities(g, 3)
community_list = list(map(sorted, community_generator))

# calculating component size
clique_size_list = []
for i in range(len(community_list)):
    clique_size_list.append(len(community_list[i]))

# data preprocessing and visualization
df = pd.DataFrame(clique_size_list)
df.columns = ['component size']
df = df.groupby(['component size']).size().reset_index(name='counts')
# 3-clique graph
plt.plot(df['component size'], df['counts'], 'r.')
plt.title('3-Clique Graph Connectivity')
plt.ylabel("count")
plt.xlabel("component size")
plt.show()

# log-log 3-clique graph
plt.plot(df['component size'], df['counts'], 'r.')
plt.title('Log-Log 3-Clique Graph Connectivity')
plt.ylabel("log count")
plt.xlabel("log component size")
plt.yscale('log')
plt.xscale('log')
plt.show()
