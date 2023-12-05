import math

class Node:
    def __init__(self, bound, path, cost, level):
        self.bound = bound
        self.level = level
        self.cost = cost
        self.path = path

    def __lt__(self, other):
    # Define a comparação para que heapq possa ordenar primeiro pelo nível e, em caso de empate no nível, pela 'bound'
      if self.level == other.level:
        return self.bound < other.bound
      return self.level < other.level
    
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

# Estimativa quando apenas o primeiro vértice foi adicionado
def first_bound(M):
  bound_cost = 0
  for e in M:
    bound_cost += (e[0] + e[1])

  return math.ceil(bound_cost/2)

def cycle_cost(A, path):
  cost = 0
  for i in range(len(path)-1):
    v = path[i]
    w = path[i+1]
    edge_cost = A[v][w]
    cost += edge_cost

  return cost + A[path[-1]][path[0]]

# Lower Bound visto em sala usando as duas menores arestas
def lower_bound(A, path, bound_parent, M):
  new_bound = bound_parent
  n = len(path)
  if n == len(M):
    return cycle_cost(A, path)

  v = path[n-2]
  w = path[n-1]

  first_min_v = M[v][0]
  second_min_v = M[v][1]

  first_min_w = M[w][0]
  second_min_w = M[w][1]

  #Casos iniciais e apartir de 3, talvez fosse uma boa ideia incluir o ciclo completo aqui com caso semelhante ao n==2
  if n == 2:
    #Primeiro em relação a W
    if((first_min_w != A[v][w] and second_min_w != A[v][w])):
      new_bound += (A[v][w] - second_min_w)/2
    #Segundo em relação a V
    if(first_min_v != A[v][w] and second_min_v != A[v][w]):
      new_bound += (A[v][w] - second_min_v)/2

  else:
    new_bound += (2*A[w][v] - second_min_w - first_min_v)/2

  return math.ceil(new_bound)

