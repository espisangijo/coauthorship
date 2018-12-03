from networkx.algorithms.community import greedy_modularity_communities
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

g = nx.read_edgelist('edge_list.csv', create_using=nx.Graph(), delimiter=',', nodetype=str)

# c for community
c = list(greedy_modularity_communities(g))
component_size_list = []

# calculate component size
for i in c:
    # x is a temporary variable for the community list
    x = list(sorted(i))
    component_size_list.append(len(x))

# data preprocessing and visualization
df = pd.DataFrame(component_size_list)
df.columns = ['community size']
df = df.groupby(['community size']).size().reset_index(name='counts')

# community graph
plt.plot(df['community size'], df['counts'], 'r.')
plt.title('Modularity Maximization Graph Connectivity')
plt.ylabel("count")
plt.xlabel("component size")
plt.show()

# log-log community graph
plt.plot(df['community size'], df['counts'], 'r.')
plt.title('Log-Log Modularity Maximization Graph Connectivity')
plt.ylabel("log count")
plt.xlabel("log component size")
plt.yscale('log')
plt.xscale('log')
plt.show()
