import networkx as nx
import math


# Função para calcular o ciclo de um grafo da bibiloteca NetworkX
def cycle_cost_networkx(graph, cycle):
    total_cost = 0

    # Adiciona o custo de cada aresta no ciclo
    for i in range(len(cycle) - 1):
        total_cost += graph[cycle[i]][cycle[i+1]]['weight']

    # Adiciona a última aresta que completa o ciclo
    total_cost += graph[cycle[-1]][cycle[0]]['weight']
    return math.ceil(total_cost)


# Encontrar os vértices de grau ímpar
def odd_degree_vertices(graph):
    graus = graph.degree()
    odds = [v for v, grau in graus if grau % 2 == 1]
    return odds
