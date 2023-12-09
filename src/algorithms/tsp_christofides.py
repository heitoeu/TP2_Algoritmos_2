from .tsp_approximative import *
import time


def tsp_christofides(g):
    # Monitorar o tempo
    inicio_tempo = time.time()

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

    tempo_execucao = time.time() - inicio_tempo
    print(f"Tempo de Execução: {tempo_execucao} segundos")
    # print(f"Solução:{sol} custo {approximative_best}")
    print(f"Custo {approximative_best}")

    return sol, approximative_best
