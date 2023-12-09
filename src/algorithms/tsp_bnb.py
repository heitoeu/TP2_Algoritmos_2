from .tsp_bnb_utilities import *
import heapq
import time


def tsp_bnb(A, tempo_limite=1):
    # Monitorar o tempo
    inicio_tempo = time.time()

    # Lista das duas menores arestas de cada vértice
    M = min_edges(A)
    n = len(M)

    root = Node(first_bound(M), [0], 0)
    queue = [(root)]
    best = math.inf
    sol = []

    # Roda enquanto existir nodes frutiferos
    while queue:
        cycle = math.inf
        node = heapq.heappop(queue)

        # Caso uma estimativa seja melhor que o melhor custo
        if node.bound < best:
            if node.level < n-1:
                for i in range(1, n):
                    # Apenas combinações de vértices que ainda não foram incluidos no caminho
                    if i not in node.path:
                        # Exclui permutações equivalentes computando só uma das orientações
                        if 2 in node.path and 1 not in node.path:
                            continue
                        lb = lower_bound(A, node.path + [i], node.bound, M)
                        # Se a bound é produtiva
                        if lb < best:
                            # Se não é uma folha adiciona na fila
                            if (node.level + 1 < n-2):
                                next_node = Node(
                                    lb, node.path + [i], node.level+1)
                                heapq.heappush(queue, next_node)
                            else:
                                # Se é uma folha computo o ciclo
                                cycle_path = cycle_complete(A, node.path+[i])
                                cycle = cycle_cost(A, cycle_path)
                                if (cycle < best):
                                    best = cycle
                                    sol = cycle_path

    # Parar a execução se estiver demorando muito (pior caso ainda é O(n!))
        tempo_atual = time.time() - inicio_tempo
        if tempo_atual > tempo_limite:
            print(f"Custo Mínimo: NA ({tempo_limite} segundos).")
            return None, None

    t = time.time() - inicio_tempo
    tempo_execucao = "{:.2f}".format(t)
    print(f"Tempo de Execução: {tempo_execucao} segundos")
    # print(f"Solução:{sol+[0]} custo {best}")
    print(f"Custo {best}")
    return sol, best
