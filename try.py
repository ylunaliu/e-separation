from platform import node
import networkx as nx
import numpy as np
import itertools
from checkdseparation import check_d_separation_total
from toolz import unique
# For a given graph find the e-separation relations.
graph_2 = nx.DiGraph()
graph_2.add_edges_from([("A", "D"), ("A", "C"),("C", "D"), ("B", "C")])
graph_2_hidden = list(["A"])

# Generate all the nodes

nodes = list(graph_2.nodes)

# Gnerate all combination of the nodes
def adjustformat(nodes):
    nodes_adjust_format = ''
    for node in nodes:
        nodes_adjust_format = nodes_adjust_format + node
    return(nodes_adjust_format)
nodes_adjust_format = adjustformat(nodes)

# Get all combination of two nodes
combination = list(itertools.combinations(nodes_adjust_format,2))


def powerset(input):
    output = sum([list(map(list, itertools.combinations(input, i))) for i in range(len(input) + 1)], [])
    return output


def make_z_not_overlap_with_nodes(pair, sets_z):
    new_set = sets_z
    for element in pair:
        if element in new_set:
            new_set.remove(element)

    return new_set




for i in range(len(combination)):
    # Now I get a pair of nodes I can regenerate the powerset for the nodes
    new_nodes = make_z_not_overlap_with_nodes(list(combination[i]), list(nodes))
    # print(f'This is the {i} combination nodes {combination[i]}')
    sets_z = powerset(new_nodes)
    # print(f'This is total sets z: {sets_z}')
    for j in range(len(sets_z)):
        # print(f'This is sets z{sets_z[j]}')
        w_nodes = make_z_not_overlap_with_nodes(sets_z[j], list(new_nodes))
        sets_w = powerset(w_nodes)
        sets_w = list(filter(None, sets_w))
        for k in range(len(sets_w)):
            print(f'This is set w{sets_w[k]}')
            new_graph = graph_2.copy()
            print(f'This is the nodes of graph{new_graph.nodes}')
            new_graph.remove_nodes_from(sets_w[k])
            print(f'This is the nodes of graph{new_graph.nodes}after removal of w')
            if(check_d_separation_total(new_graph, combination[i], sets_z[j])==True):
                print(f'{combination[i][0]} and {combination[i][1]} are e-separated by {sets_z[j]} upon deletion of {sets_w}')
    
        # for k in range(len(sets_w)):
        #     print(sets_w[k])
        #     new_graph = graph_2
        #     new_graph = new_graph.remove_nodes_from(list(filter(None,sets_w[k])))
        #     print(new_graph)
        #     if(check_d_separation_total(new_graph, combination[i], sets_z[j])==True):
        #         print(f'{combination[i][0]} and {combination[i][1]} are e-separated by {sets_z[j]} upon deletion of {sets_w}')



