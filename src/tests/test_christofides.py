from ..algorithms.tsp_christofides import *

# Grafo do livro
grafo_vimieiro = nx.Graph()
grafo_vimieiro.add_edges_from([(0, 1, {'weight': 4}),
                               (0, 2, {'weight': 8}),
                               (0, 3, {'weight': 9}),
                               (0, 4, {'weight': 12}),
                               (1, 2, {'weight': 6}),
                               (2, 3, {'weight': 10}),
                               (3, 4, {'weight': 7}),
                               (4, 1, {'weight': 9}),
                               (2, 4, {'weight': 11}),
                               (1, 3, {'weight': 8})])


tsp_christofides(grafo_vimieiro)
