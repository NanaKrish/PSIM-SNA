import csv
from pathlib import Path

import networkx
from networkx.readwrite import json_graph

from psim.agents.entity import Person, Location


def load_user_data(file_path: str):
    path = Path(file_path).absolute()
    with open(path, 'r') as f:
        reader = csv.reader(f)
        for data in reader:
            yield Person(data[0], int(data[1]), Location(float(data[2]), float(data[3])))


def get_cytoscape_elts(G: networkx.Graph):
    """
    Returns the elements as required in a format for dash-cytoscape
    """
    cjs = json_graph.cytoscape_data(G)
    elements = cjs['elements']['nodes'] + cjs['elements']['edges']

    for elt in elements:
        d = elt['data']
        # networkx sets the value attribute to the type passed when creating the 
        # node. It may not be passable as json, which will create errors when serialising
        # as JSON. So we replace it
        person = d.pop('value', '')
        if isinstance(person, Person) and not person.healthy :
            d['infected'] = 'true'
        else: 
            d['infected'] = 'false'

        d['label'] = str(person)

        # Do the same as above if it is an edge
        if d.get('source', None):
            d['source'] = str(d['source'])

        if d.get('target', None):
            d['target'] = str(d['target'])
    return elements