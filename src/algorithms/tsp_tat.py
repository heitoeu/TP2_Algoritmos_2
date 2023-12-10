from .tsp_approximative import *
import time


def tsp_tat(g):
    # Monitorar o tempo
    inicio_tempo = time.time()

    root = 1
    # Computa a minimum spanning tree
    mst = nx.minimum_spanning_tree(g)

    # Caminhamento preorder para obter o ciclo hamiltoniano
    preorder_result = list(nx.dfs_preorder_nodes(mst, root))

    # Calcula o custo e completa o ciclo com a raiz
    approximative_best = cycle_cost_networkx(g, preorder_result)
    sol = preorder_result + [root]

    t = time.time() - inicio_tempo
    tempo_execucao = "{:.2f}".format(t)

    return approximative_best, tempo_execucao
