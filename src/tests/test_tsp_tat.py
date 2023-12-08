from ..algorithms.tsp_tat import *

# Grafo do livro
grafo_vimieiro = Graph()
grafo_vimieiro.add_vertices(5)
grafo_vimieiro.add_edge(0, 1, weight=4)
grafo_vimieiro.add_edge(0, 2, weight=8)
grafo_vimieiro.add_edge(0, 3, weight=9)
grafo_vimieiro.add_edge(0, 4, weight=12)
grafo_vimieiro.add_edge(1, 2, weight=6)
grafo_vimieiro.add_edge(2, 3, weight=10)
grafo_vimieiro.add_edge(3, 4, weight=7)
grafo_vimieiro.add_edge(4, 1, weight=9)
grafo_vimieiro.add_edge(2, 4, weight=11)
grafo_vimieiro.add_edge(1, 3, weight=8)


print("Clique: ", grafo_vimieiro)

path, value = mst = tsp_tat(grafo_vimieiro)
print(f"Caminho encontrado: {path} com peso de {value}")
