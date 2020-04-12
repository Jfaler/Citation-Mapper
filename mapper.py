'''
Programmer: Justin Faler
Date: 4/8/2020
Description: PDF Citation Map
'''

import numpy as np
import networkx as nx
import matplotlib as mpl
import pdfminer, re, sys, os, time, csv
import matplotlib.pyplot as plt
from refextract import extract_references_from_file

plt.rcParams["figure.facecolor"] = "#333333"

citation_map = nx.DiGraph(directed=True)
references = extract_references_from_file('/home/user/Documents/Books/example.pdf')

options = {
    'node_color': '#36DBCA',
    'node_size': 150,
    'width': 0.2,
    'alpha': 1,
    'arrowstyle': '-|>',
    'arrowsize': 15,
}

base = os.path.basename('/home/user/Documents/Books/example.pdf')
name = os.path.splitext(base)[0]

i = 1

while (i < 30):
    i = i + 1
    citations = references[i]['raw_ref']
    print(citations)
    citation_map.add_edge(name, *citations)
    citation_map.add_nodes_from(citations)

# Layout
pos = nx.spring_layout(citation_map)
nx.draw_networkx(citation_map, pos, arrows=True, **options)
plt.tight_layout()
plt.axis('off')
plt.show()
