import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

g = nx.read_edgelist('edge_list.csv', create_using=nx.Graph(), delimiter=',', nodetype=str)

# measure network connectivity and put it in a list
component_size_list = [len(c) for c in sorted(nx.connected_components(g), key=len, reverse=True)]

# aggregate by count
df = pd.DataFrame(component_size_list)
df.columns = ['node number']
df = df.groupby(['node number']).size().reset_index(name='counts')

# plot log-log graph between log n(i) and log i
plt.title("Log-Log Network Connectivity")
plt.plot(df['node number'], df['counts'], 'r.')
plt.ylabel("log n(i)")
plt.xlabel("log i")
plt.yscale('log')
plt.xscale('log')
plt.show()
