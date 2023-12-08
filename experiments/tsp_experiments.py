from src.algorithms.tsp_bnb import *
from src.algorithms.tsp_tat import *
from src.calculate.distance import euclidean_distance
import os


def read_tsp_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    lines = content.split('\n')

    # Encontre a linha que marca o início das coordenadas dos nós
    try:
        node_coord_section_index = lines.index("NODE_COORD_SECTION") + 1
    except ValueError:
        print("Erro: NODE_COORD_SECTION não encontrado no arquivo.")
        return []

    # Obtenha as coordenadas dos nós como uma lista de tuplas
    node_coordinates = []
    for line in lines[node_coord_section_index:]:
        if line.strip() and line.upper() != "EOF":  # Ignorar linhas em branco e a linha "EOF"
            try:
                parts = line.split()
                node_coordinates.append((float(parts[1]), float(parts[2])))
            except (ValueError, IndexError):
                print(f"Erro ao processar a linha: {line}")

    return node_coordinates


def calculate_distance_matrix(node_coordinates):
    n = len(node_coordinates)
    distance_matrix = [[0] * n for _ in range(n)]

    # Preencha a matriz de adjacência com as distâncias euclidianas
    for i in range(n):
        for j in range(n):
            if i != j:
                distance_matrix[i][j] = euclidean_distance(
                    node_coordinates[i], node_coordinates[j])

    return distance_matrix


def create_igraph_from_distance_matrix(node_coordinates):
    num_nodes = len(node_coordinates)

    # Cria um grafo ponderado
    g = Graph()
    g.add_vertices(num_nodes)

    # Adiciona as arestas ponderadas com as distâncias sem duplicatas
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            distance = euclidean_distance(
                node_coordinates[i], node_coordinates[j])
            g.add_edge(i, j, weight=float(distance))

    return g


instance = ['a0', 'a280', 'berlin52', 'bier127', 'fl417', 'fl1400', 'fl1577']
for i in instance:
    print("Instancia: ", i)

    file_path = os.path.abspath(os.path.join('lib', f'{i}.tsp'))
    node_coordinates = read_tsp_file(file_path)
    print("Criando lista de adjacencia")
    graph_matrix = calculate_distance_matrix(node_coordinates)
    print("Lista de adjacencia criada!")

    print("Criando Grafo da iGraph")
    graph_list = create_igraph_from_distance_matrix(node_coordinates)
    print("Grafo da iGraph criado criado!")

    # Algoritmo TSP_BNB
    print("TSP_BNB")
    best_path, best_cost = tsp_bnb(graph_matrix)

    # Algoritmo TSP_TAT
    print("TSP_TAT")
    best_path, best_cost = tsp_tat(graph_list)
