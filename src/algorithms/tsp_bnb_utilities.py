import math


class Node:
    def __init__(self, bound, path, level):
        self.bound = bound
        self.level = level
        self.path = path

    def __lt__(self, other):
        # Define a comparação para que heapq possa ordenar primeiro pelo nível e, em caso de empate no nível, pela 'bound'
        if self.level == other.level:
            return self.bound < other.bound
        return self.level > other.level


# Retorna uma lista das duas menores arestas de cada vértice
def min_edges(A):
    n = len(A)
    smallest_edges_list = []

    for i in range(n):
        aux = []
        for j in range(n):
            if A[i][j] != 0:
                aux.append(A[i][j])
        aux.sort()
        smallest_edges_list.append((aux[0], aux[1]))
    return smallest_edges_list


# Estimativa para a raiz
def first_bound(M):
    bound_cost = 0
    for e in M:
        bound_cost += (e[0] + e[1])
    return math.ceil(bound_cost/2)


# Termina o ciclo das folhas
def cycle_complete(A, path):
    for i in range(len(A)):
        if i not in path:
            x = i
            return path + [x]


# Calcula o custo do ciclo
def cycle_cost(A, path):
    cost = 0
    for i in range(len(path)-1):
        v = path[i]
        w = path[i+1]
        edge_cost = A[v][w]
        cost += edge_cost
    return math.ceil(cost + A[path[-1]][path[0]])


# Lower Bound visto em sala usando as duas menores arestas de cada vértice
def lower_bound(A, path, bound_parent, M):
    new_bound = bound_parent
    n_path = len(path)

    v = path[n_path-2]
    w = path[n_path-1]

    first_min_v = M[v][0]
    second_min_v = M[v][1]

    first_min_w = M[w][0]
    second_min_w = M[w][1]

    # Primeiro em relação a W
    if ((first_min_w != A[v][w] and second_min_w != A[v][w])):
        new_bound = (2*new_bound + A[v][w] - second_min_w)/2
        # Segundo em relação a V
    if (first_min_v != A[v][w] and second_min_v != A[v][w]):
        new_bound = (2*new_bound + A[v][w] - second_min_v)/2

    return math.ceil(new_bound)
