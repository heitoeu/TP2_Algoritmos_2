from igraph import Graph


# Caminhamento preorder recursivo
def pre_order(g, root, visited, result):
    visited[root] = True
    result.append(root)
    for n in g.neighbors(root):
        if not visited[n]:
            pre_order(g, n, visited, result)


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

    return total_cost
