from src.algorithms.tsp_bnb import *
from src.algorithms.tsp_tat import *
from src.algorithms.tsp_christofides import *
from src.algorithms.distance import euclidean_distance
import os
import csv


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


def read_dataset_names(file_path):
    dataset_names = []

    with open(file_path, 'r') as file:
        # Pular a primeira linha, pois contém os cabeçalhos
        next(file)

        for line in file:
            # Dividir a linha usando tabulação como delimitador
            parts = line.split('\t')

            # Adicionar o nome do dataset à lista
            dataset_names.append(parts[0])

    return dataset_names


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


def create_networkx_graph(node_coordinates):
    num_nodes = len(node_coordinates)
    g = nx.Graph()

    g.add_nodes_from(range(num_nodes))

    # Computar as arestas e seus pesos na lista
    edges = [(i, j, euclidean_distance(node_coordinates[i], node_coordinates[j]))
             for i in range(num_nodes) for j in range(i + 1, num_nodes)]

    # Adiciona as arestas ao grafo com os pesos
    g.add_weighted_edges_from(edges)

    return g


data_set_path = os.path.abspath(
    os.path.join('experiments', f'tp2_datasets.txt'))
instance = read_dataset_names(data_set_path)

# Caminho para o arquivo CSV de saída
output_csv_path = os.path.abspath(os.path.join('output', 'resultados_tsp.csv'))

# Abrir o arquivo CSV para escrita
with open(output_csv_path, 'w', newline='') as csvfile:
    # Criar o objeto de escrita CSV
    csv_writer = csv.writer(csvfile)

    # Escrever cabeçalhos no arquivo CSV
    csv_writer.writerow(
        ['Instance', 'Algorithm', 'Cost', 'Time', 'Memory'])

    for i in instance:

        file_path = os.path.abspath(os.path.join('lib', f'{i}.tsp'))

        # Criando os Grafos
        node_coordinates = read_tsp_file(file_path)
        graph_matrix = calculate_distance_matrix(node_coordinates)
        graph_list = create_networkx_graph(node_coordinates)

        # Algoritmo TSP_BNB
        best_cost, time, memory = tsp_bnb(graph_matrix)
        csv_writer.writerow([i, 'TSP_BNB', best_cost, time, memory])

        # Algoritmo TSP_TAT
        best_cost, time, memory = tsp_tat(graph_list)
        csv_writer.writerow([i, 'TSP_TAT', best_cost, time, memory])

        # Algoritmo TSP_CHRIS
        best_cost, time, memory = tsp_christofides(graph_list)
        csv_writer.writerow([i, 'TSP_CHRIS', best_cost, time, memory])

        # csv_writer.writerow('\n')
