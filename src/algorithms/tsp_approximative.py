from igraph import *
import math


# Caminhamento preorder iterativo
def pre_order_iterative(g, root):
    visited = [False] * g.vcount()
    result = []
    stack = [root]

    while stack:
        current_vertex = stack.pop()

        if not visited[current_vertex]:
            visited[current_vertex] = True
            result.append(current_vertex)
            # Empilhe os vizinhos não visitados do vértice atual
            # stack.extend(n for n in g.neighbors(current_vertex) if not visited[n])
            stack.extend(n for n in reversed(
                g.neighbors(current_vertex)) if not visited[n])

    return result


# Função para calcular o ciclo de um grafo da bibiloteca iGraph
def cycle_cost_igraph(graph, cycle):
    total_cost = 0

    # Adiciona o custo de cada aresta no ciclo
    for i in range(len(cycle) - 1):
        edge = graph.es.find(_source=cycle[i], _target=cycle[i+1])
        total_cost += edge['weight']

    # Adiciona a última aresta que completa o ciclo
    edge = graph.es.find(_source=cycle[-1], _target=cycle[0])
    total_cost += edge['weight']

    return math.ceil(total_cost)
