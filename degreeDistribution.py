import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import numpy as np
import collections

g = nx.read_edgelist('edge_list.csv', create_using=nx.Graph(), delimiter=',', nodetype=str)

# calculate degree of each node
degs = sorted([d for n, d in g.degree()], reverse=True)
countCol = collections.Counter(degs)
deg, cnt = zip(*countCol.items())

print(len(g.nodes))

# plot degree vs. count
fig, ax = plt.subplots()
plt.scatter(deg, cnt)
plt.title("Degree Distribution")
plt.ylabel("k(j)")
plt.xlabel("j")
plt.show()

# plot log(degree) vs. log(count)
plt.scatter(deg, cnt)
plt.title("Log-Log Degree Distribution")
plt.ylabel("log k(j)")
plt.xlabel("log j")
plt.xscale('log')
plt.yscale('log')
plt.show()
