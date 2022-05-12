from platform import node
import networkx as nx
import numpy as np
import itertools
from checkdseparation import check_d_separation_total
from toolz import unique

def e_separation_list(graph, hidden_nodes):
    # Graph is a directed graph object
    # hidden_nodes is a list contains the hidden variables in the from ["a", "b" ...]
    nodes = list(graph.nodes)
    
    if(hidden_nodes!=[]):
        for node in hidden_nodes:
            nodes.remove(node)

    # Now we have a way to check if given two nodes and a set z, we need all cominbination of two nodes and set z and store it to a table
    def adjustformat(nodes):
        nodes_adjust_format = ''
        for node in nodes:
            nodes_adjust_format = nodes_adjust_format + node
        return(nodes_adjust_format)
    nodes_adjust_format = adjustformat(nodes)

    # Get all combination of two nodes
    combination = list(itertools.combinations(nodes_adjust_format,2))

    # Get all combibation for set Z
    def powerset(input):
        output = sum([list(map(list, itertools.combinations(input, i))) for i in range(len(input) + 1)], [])
        return output
    # Get all the nodes:
    for i in range(len(combination)):
        # Now I get a pair of nodes I can regenerate the powerset for the nodes
        new_nodes = make_z_not_overlap_with_nodes(list(combination[i]), list(nodes))
        sets_z = powerset(new_nodes)
        for j in range(len(sets_z)):
            w_nodes = make_z_not_overlap_with_nodes(sets_z[j], list(new_nodes))
            sets_w = powerset(w_nodes)
            sets_w = list(filter(None, sets_w))
            for k in range(len(sets_w)):
                new_graph = graph.copy()
                new_graph.remove_nodes_from(sets_w[k])
                # print(f'upon remove of {sets_w[k]}')
                # print(f'look at combination {combination[i]}')
                if(check_d_separation_total(new_graph, combination[i], sets_z[j])==True):
                    print(f'{combination[i][0]} and {combination[i][1]} are e-separated by {sets_z[j]} upon deletion of {sets_w[k]}')


def make_z_not_overlap_with_nodes(pair, sets_z):
    new_set = sets_z
    for element in pair:
        if element in new_set:
            new_set.remove(element)

    return new_set

if __name__ == "__main__":
   # graph = nx.DiGraph()
   # graph.add_edges_from([("x", "a"), ("a", "b"), ("a", "e"), ("b", "c"), ("b", "d"), ("d", "e")])
    # descendants = list(nx.descendants(graph,"a"))
    # print(descendants)
    # z = ["h"]
    # print(set(descendants).isdisjoint(z))

    # Need to define the 11 graphs
    #!!! Don't work: the graph fall apart 
    #2 Bell's seno
    # graph_2 = nx.DiGraph()
    # graph_2.add_edges_from([("B", "E"), ("A", "E"), ("A", "D"), ("C", "D")])
    # graph_2_hidden = list(["A"])
    # e_separation_list(graph_2,graph_2_hidden)

#     The e-separation for graph 2 is
# B and D are e-separated by [] upon deletion of ['E'] 
# B and D are e-separated by [] upon deletion of ['C']
# B and D are e-separated by [] upon deletion of ['E', 'C'] 
# B and D are e-separated by ['C'] upon deletion of ['E']
# B and C are e-separated by [] upon deletion of ['E'] .
# B and C are e-separated by [] upon deletion of ['D']
## I don't have B and C are e-separated by [] upon deletion of ['E' and 'D']
## Maybe I should also considering adding empty set to W
# B and C are e-separated by ['E'] upon deletion of ['D']
# B and C are e-separated by ['D'] upon deletion of ['E']
# E and C are e-separated by [] upon deletion of ['B']
# E and C are e-separated by [] upon deletion of ['D']
# E and C are e-separated by [] upon deletion of ['B', 'D']
# E and C are e-separated by ['B'] upon deletion of ['D']


#     # #3 Unrelated confounder Correct?

    # graph_3 = nx.DiGraph()
    # graph_3.add_edges_from([("A", "E"), ("C", "E"), ("C", "D"), ("A", "C"), ("B", "C"), ("B", "D")])
    # graph_3_hidden = list(["A", "B"])
    # e_separation_list(graph_3,graph_3_hidden)

#     The e-separation for graph 3 is
#     E and D are e-separated by [] upon deletion of ['C']

    # # Graph 1 ?
    # graph_1 = nx.DiGraph()
    # graph_1.add_edges_from([("A", "D"), ("A", "C"),("C", "D"), ("B", "C")])
    # graph_1_hidden = list(["A"])
    # e_separation_list(graph_1, graph_1_hidden)

#     The e-separation for graph 1 is
#     D and B are e-separated by [] upon deletion of ['C']


    # Graph 4 maybe? Also can check for descendant?
    # graph_4 = nx.DiGraph()
    # graph_4.add_edges_from([("A", "F"), ("A", "C"), ("B", "C"), ("B", "E"), ("D", "E"), ("C", "F"), ("E", "F")])
    # graph_4_hidden = list(["A", "B"])
    # e_separation_list(graph_4, graph_4_hidden)

#     The e-separation for graph 4 is
    # F and D are e-separated by [] upon deletion of ['E']
    # F and D are e-separated by [] upon deletion of ['C', 'E']
    # F and D are e-separated by ['C'] upon deletion of ['E']
    # F and D are e-separated by ['E'] upon deletion of ['C']
    # C and D are e-separated by [] upon deletion of ['F']
    # C and D are e-separated by [] upon deletion of ['E']
    # C and D are e-separated by [] upon deletion of ['F', 'E']
    # C and D are e-separated by ['F'] upon deletion of ['E']


    # Graph 5 
    # graph_5 = nx.DiGraph()
    # graph_5.add_edges_from([("A", "E"), ("A", "F"), ("E", "F"), ("B", "F"), ("B", "D"), ("D", "E"), ("C", "D")])
    # graph_5_hidden = list(["A", "B"])
    # e_separation_list(graph_5, graph_5_hidden)

#     The e-separation for graph 5 is
# E and C are e-separated by [] upon deletion of ['D']
# E and C are e-separated by [] upon deletion of ['F', 'D']
# E and C are e-separated by ['F'] upon deletion of ['D']
# E and C are e-separated by ['D'] upon deletion of ['F']
# F and C are e-separated by [] upon deletion of ['E']
# F and C are e-separated by [] upon deletion of ['D']
# F and C are e-separated by [] upon deletion of ['E', 'D']
# F and C are e-separated by ['E'] upon deletion of ['D']


    # Graph 16
    # graph_16 = nx.DiGraph()
    # graph_16.add_edges_from([("A", "E"), ("A", "F"), ("B", "F"), ("B", "D"), ("C", "D"), ("C", "E"), ("D", "E")])
    # graph_16_hidden = list(["A", "B"])
    # e_separation_list(graph_16, graph_16_hidden)

#     The e-separation for graph 16 is
# F and C are e-separated by [] upon deletion of ['E']
# F and C are e-separated by [] upon deletion of ['D']
# F and C are e-separated by [] upon deletion of ['E', 'D']
    
    
    # Graph 17
    # graph_17 = nx.DiGraph()
    # graph_17.add_edges_from([("A", "F"), ("A", "C"), ("B", "C"), ("B", "E"), ("D", "E"), ("C", "F"), ("C", "E"), ("E", "F")])
    # graph_17_hidden = list(["A", "B"])
    # e_separation_list(graph_17, graph_17_hidden)

#    The e-separation for graph 17 is
# F and D are e-separated by [] upon deletion of ['E']
# F and D are e-separated by [] upon deletion of ['C', 'E']
# F and D are e-separated by ['C'] upon deletion of ['E']
# F and D are e-separated by ['E'] upon deletion of ['C']
# C and D are e-separated by [] upon deletion of ['F']
# C and D are e-separated by [] upon deletion of ['E']
# C and D are e-separated by [] upon deletion of ['F', 'E']
# C and D are e-separated by ['F'] upon deletion of ['E']



    # Graph 18

    # graph_18 = nx.DiGraph()
    # graph_18.add_edges_from([("A", "F"), ("A", "D"), ("B", "D"), ("B", "E"), ("D", "E"), ("C", "D"), ("C", "E"), ("E", "F")])
    # graph_18_hidden = list(["A", "C"])
    # e_separation_list(graph_18, graph_18_hidden)

#     The e-separation for graph 18 is
# F and B are e-separated by [] upon deletion of ['E']
# F and B are e-separated by [] upon deletion of ['D', 'E']
# F and B are e-separated by ['E'] upon deletion of ['D']

    # Graph 19

    # graph_19 = nx.DiGraph()
    # graph_19.add_edges_from([("A", "F"), ("A", "D"), ("B", "C"), ("B", "E"), ("D", "E"), ("C", "D"), ("C", "E"), ("E", "F")])
    # graph_19_hidden = list(["A", "C"])
    # e_separation_list(graph_19, graph_19_hidden)

#     The e-separation for graph 19 is
# F and B are e-separated by [] upon deletion of ['E']
# F and B are e-separated by [] upon deletion of ['D', 'E']
# F and B are e-separated by ['E'] upon deletion of ['D']


    # Graph 20
    # graph_20 = nx.DiGraph()
    # graph_20.add_edges_from([("A", "E"), ("A", "F"), ("B", "F"), ("B", "D"), ("C", "D"), ("D", "E")])
    # graph_20_hidden = list(["A", "B"])
    # e_separation_list(graph_20, graph_20_hidden)

# E and C are e-separated by [] upon deletion of ['D']
# E and C are e-separated by [] upon deletion of ['F', 'D']
# E and C are e-separated by ['F'] upon deletion of ['D']
# E and C are e-separated by ['D'] upon deletion of ['F']
# F and C are e-separated by [] upon deletion of ['E']
# F and C are e-separated by [] upon deletion of ['D']
# F and C are e-separated by [] upon deletion of ['E', 'D']
# F and C are e-separated by ['E'] upon deletion of ['D']

    # graph1 = nx.DiGraph()
    # graph1.add_edges_from([("s", "a"), ("l", "a"), ("l", "b"), ("t", "b")])
    # print(graph1.nodes)
    # hidden_nodes = ["b"]
    # e_separation_list(graph1, hidden_nodes)


# Graphs in papaer 
    # graph_c = nx.DiGraph()
    # graph_c.add_edges_from([("A", "D"), ("D", "B"), ("U", "D"), ("U", "B")])
    # graph_c_hidden = list(["U"])
    # e_separation_list(graph_c, graph_c_hidden)


# TCF 

    # graph_20 = nx.DiGraph()
    # graph_20.add_edges_from([("p", "a"), ("p", "d"), ("u", "a"), ("u", "c"), ("v", "b"), ("v", "c"), ("a", "b"),("b", "c"), ("c", "d")])
    # graph_20_hidden_nodes = ["p", "u", "v"]
    # e_separation_list(graph_20, graph_20_hidden_nodes)

    # None