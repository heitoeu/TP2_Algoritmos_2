from src.algorithms.tsp_bnb import tsp_bnb
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
                distance_matrix[i][j] = euclidean_distance(node_coordinates[i], node_coordinates[j])

    return distance_matrix

#berlin52
file_path = os.path.abspath(os.path.join('lib', 'berlin14.tsp'))
node_coordinates = read_tsp_file(file_path)
distance_matrix = calculate_distance_matrix(node_coordinates)

best_path, best_cost = tsp_bnb(distance_matrix)

print("Melhor caminho:", best_path)
print("Custo mínimo:", best_cost)
