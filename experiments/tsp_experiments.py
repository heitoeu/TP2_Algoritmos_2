from src.algorithms.tsp_bnb import *
from src.algorithms.tsp_tat import *
from src.algorithms.tsp_christofides import *
from src.algorithms.distance import euclidean_distance
import os
import csv
import time as t
import tracemalloc


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


def read_dataset(file_path):
    dataset_info = []

    with open(file_path, 'r') as file:
        # Pular a primeira linha, pois contém os cabeçalhos
        next(file)

        for line in file:
            # Dividir a linha usando tabulação como delimitador
            parts = line.split('\t')

            # Adicionar o nome do dataset e o limiar à lista
            dataset_info.append({
                'name': parts[0],
                'nodes': int(parts[1]),
                # Avaliar a expressão para lidar com casos como [22204,22249]
                'threshold': eval(parts[2])
            })

    return dataset_info


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


def create_networkx_graph(node_coordinates, timeout=600):
    num_nodes = len(node_coordinates)
    g = nx.Graph()

    g.add_nodes_from(range(num_nodes))

    # Obtém o tempo inicial
    start_time = t.time()

    # Loop de adição de arestas
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            # Verifica o tempo decorrido em cada iteração
            elapsed_time = t.time() - start_time

            # Se o tempo excedeu o limite, retorna None
            if elapsed_time > timeout:
                return None

            # Adiciona a aresta ao grafo com o peso
            g.add_edge(i, j, weight=euclidean_distance(
                node_coordinates[i], node_coordinates[j]))

    return g


data_set_path = os.path.abspath(
    os.path.join('experiments', f'tp2_datasets.txt'))

dataset_info = read_dataset(data_set_path)

# Caminho para o arquivo CSV de saída
output_csv_path = os.path.abspath(os.path.join('output', 'resultados_tsp.csv'))

# Abrir o arquivo CSV para escrita
with open(output_csv_path, 'w', newline='') as csvfile:
    # Criar o objeto de escrita CSV
    csv_writer = csv.writer(csvfile)

    # Escrever cabeçalhos no arquivo CSV
    csv_writer.writerow(
        ['Algorithm', 'Instance', 'Nodes', 'Limiar', 'Cost', 'Quality', 'Time(sec)', 'Memory(MB)'])

    for info in dataset_info:
        # Obtendo infos de cada instância
        dataset_name = info['name']
        dataset_nodes = info['nodes']
        dataset_limiar = info['threshold']
        if (type(dataset_limiar) == list):
            dataset_limiar = dataset_limiar[1]

        print("Executando Instancia: ", dataset_name)

        file_path = os.path.abspath(os.path.join('lib', f'{dataset_name}.tsp'))
        # Criando os Grafos
        node_coordinates = read_tsp_file(file_path)
        graph_matrix = calculate_distance_matrix(node_coordinates)
        graph_list = create_networkx_graph(node_coordinates)

        # Algoritmo TSP_BNB
        tracemalloc.reset_peak()
        tracemalloc.start()
        # TSP_BNB
        best_cost, time = tsp_bnb(graph_matrix)

        current_memory, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        memory = round(peak_memory / (1024 ** 2), 2)

        quality = best_cost/dataset_limiar if best_cost != "NA" else "NA"
        if type(quality) != str:
            quality = round(quality, 2)
        csv_writer.writerow(
            ['Branch and Bound', dataset_name, dataset_nodes, dataset_limiar, best_cost, quality, time, memory])

        # Algoritmo TSP_TAT
        if (graph_list != None):
            tracemalloc.reset_peak()
            tracemalloc.start()
            # TSP_TAT
            best_cost, time = tsp_tat(graph_list)

            current_memory, peak_memory = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            memory = round(peak_memory / (1024 ** 2), 2)

            quality = best_cost/dataset_limiar if best_cost != "NA" else "NA"
            if type(quality) != str:
                quality = round(quality, 2)
            csv_writer.writerow(
                ['Twice Around the Tree', dataset_name, dataset_nodes, dataset_limiar, best_cost, quality, time, memory])
        else:
            csv_writer.writerow(
                ['Twice Around the Tree', dataset_name, dataset_nodes, dataset_limiar, "NA", "NA", "NA", "NA"])

        # Algoritmo TSP_CHRIS
        if (graph_list != None):
            tracemalloc.reset_peak()
            tracemalloc.start()
            # TSP_CHRIS
            best_cost, time = tsp_christofides(graph_list)

            current_memory, peak_memory = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            memory = round(peak_memory / (1024 ** 2), 2)

            quality = best_cost/dataset_limiar if best_cost != "NA" else "NA"
            if type(quality) != str:
                quality = round(quality, 2)
            csv_writer.writerow(
                ['Christofides', dataset_name, dataset_nodes, dataset_limiar, best_cost, quality, time, memory])
        else:
            csv_writer.writerow(
                ['Christofides', dataset_name, dataset_nodes, dataset_limiar, "NA", "NA", "NA", "NA"])
