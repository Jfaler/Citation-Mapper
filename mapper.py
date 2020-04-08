'''
Programmer: Justin Faler
Date: 4/7/2020
Description: PDF Citation Map
'''
from tqdm import tqdm
import numpy as np
import networkx as nx
import pdfminer, re, sys, os, time, csv
import matplotlib.pyplot as plt
from refextract import extract_references_from_file


citation_map = nx.Graph(directed=True)
references = extract_references_from_file('/home/gadfly/Documents/Books/example.pdf')
#print(references)
options = {
    'node_color': '#28a7ea',
    'node_size': 600,
    'width': 1,
    'arrowstyle': '-|>',
    'arrowsize': 25,
}


i = 1
base = os.path.basename('/home/gadfly/Documents/Books/example.pdf')
name = os.path.splitext(base)[0]

while (i < 10):
    i = i + 1
    citations = references[i]['raw_ref']
    print(citations)
    citation_map.add_edge(name, *citations)
    citation_map.add_nodes_from(citations)




# Layout
nx.draw_networkx(citation_map, arrows=True, **options)
plt.show()
