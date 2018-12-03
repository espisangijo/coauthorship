import csv
import networkx as nx

# open the file
with open('project_dataset.csv', 'r') as f:
    g = nx.Graph()
    data = csv.reader(f, delimiter=',')
    for text in data:
        text_list = []
        # split by '&''
        text_list = text[3].split('&')
        text_list = sorted(text_list)
        for i in range(len(text_list)):
            # capitalize to make sure there is no duplicate
            text_list[i] = text_list[i].strip().capitalize()
        # add to node list
        g.add_nodes_from(text_list)
        # if author > 1, there is an edge
        if(len(text_list) > 1):
            # loop through the whole list to get all the combination of edges
            for i in range(len(text_list)):
                for j in range(i + 1, len(text_list)):
                    g.add_edge(text_list[i], text_list[j])
    # create a csv file from the edges retrieved
    nx.write_edgelist(g, 'edge_list.csv', delimiter=',', data=False)
