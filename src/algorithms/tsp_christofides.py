from .tsp_approximative import *
import time


def tsp_christofides(g):
    # Monitorar o tempo
    inicio_tempo = time.time()

    root = 0
    # Computa a minimum spanning tree
    mst = nx.minimum_spanning_tree(g)

    # Vértices de grau ímpar da árvore geradora
    odd_vertices = odd_degree_vertices(mst)

    # Grafo induzido gerado pelos graus impares
    induzido = g.subgraph(odd_vertices)
    # Computar matching perfeito de peso mínimo
    matching_edges = nx.min_weight_matching(induzido)

    # Juntar a Árvore com as Arestas do Matching
    mst.add_edges_from(matching_edges)

    # Caminhamento preorder para obter o ciclo hamiltoniano
    preorder_result = list(nx.dfs_preorder_nodes(mst))

    # Calcula o custo e completa o ciclo com a raiz
    approximative_best = cycle_cost_networkx(g, preorder_result)
    sol = preorder_result + [root]

    t = time.time() - inicio_tempo
    tempo_execucao = "{:.2f}".format(t)
    print(f"Tempo de Execução: {tempo_execucao} segundos")
    print(f"Custo {approximative_best}")

    return sol, approximative_best
