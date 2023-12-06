from igraph import Graph

def tsp_tat(g):
    mst = g.spanning_tree(weights=g.es["weight"])
    print(type(mst))

    return

g = Graph(directed=False)
g.add_vertices(4)
g.add_edges([(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)])
g.es["weight"] = [2, 3, 1, 4, 5, 6]

tsp_tat(g)
print(g)