from .tsp_approximative import *


def tsp_tat(g):
    root = 0
    # Computa a minimum spanning tree
    mst = g.spanning_tree(weights=g.es["weight"])

    # Caminhamento preorder para obter o ciclo hamiltoniano
    visited = [False] * g.vcount()
    preorder_result = []
    pre_order(mst, root, visited, preorder_result)

    # Calcula o custo e completa o ciclo com a raiz
    approximative_best = cycle_cost_igraph(g, preorder_result)
    sol = preorder_result + [root]

    return sol, approximative_best
