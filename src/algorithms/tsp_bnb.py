from .tsp_bnb_utilities import *
import time

def tsp_bnb(A, tempo_limite=240):
  #Monitorar o tempo
  inicio_tempo = time.time()

  M = min_edges(A)
  n = len(M)

  root = Node(first_bound(M), [0], math.inf, 0) #lb, path, cost, path
  queue = [(root)]

  best = math.inf
  sol = []

  print("Lower Bound da Raiz: ", root.bound)

  while queue:
    node = queue.pop()

    if node.level == n-1:      #Se o node concluiu um ciclo
      if node.cost < best:
        best = node.cost
        sol =  node.path + [0]
        #print("Melhor caminho até o momento:", sol)
        #print("Custo mínimo até o momento:", best)

    elif node.bound < best:  #Caso uma estimativa seja melhor que o melhor custo até o momento
      for i in range(1, n):
        # Vértices que ainda não foram incluidos
          if i not in node.path:
              # Exclui permutações equivalentes computando só uma das orientações
              if 2 in node.path and 1 not in node.path:
                continue
              lb = lower_bound(A, node.path + [i], node.bound, M)
              if lb < best:
                if(node.level + 1 != n-1):
                  queue.append(Node(lb, node.path + [i], math.inf, node.level+1))
                else:
                  queue.append(Node(lb, node.path + [i], lb, node.level+1))

  #Parar a execução se estiver demorando muito (pior caso ainda é O(n!))
    tempo_atual = time.time() - inicio_tempo
    if tempo_atual > tempo_limite:
            print(f"Custo Mínimo: NA ({tempo_limite} segundos).")
            return None, None

  tempo_execucao = time.time() - inicio_tempo
  print(f"Tempo de Execução: {tempo_execucao} segundos")
  return sol, best