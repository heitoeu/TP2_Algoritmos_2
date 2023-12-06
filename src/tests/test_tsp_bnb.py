from ..algorithms.tsp_bnb import tsp_bnb

graph1 = [[0, 3, 1, 5, 8],
          [3, 0, 6, 7, 9],
          [1, 6, 0, 4, 2],
          [5, 7, 4, 0, 3],
          [8, 9, 2, 3, 0]]

best_path, best_cost = tsp_bnb(graph1)

print("Melhor caminho:", best_path)
print("Custo mínimo:", best_cost)
