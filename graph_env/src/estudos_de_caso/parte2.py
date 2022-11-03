import sys

sys.path.insert(1, "C:/Users/gabri/Desktop/graph_library/graph_env/src")

from typing import List, Tuple, Any
from data_structures.search_vertex import Vertice
from data_structures.adjacency_vector import VetorAdj
from searches.dijkstra import dijkstra_com_heap, dijkstra_com_vetor
from file_utils.file_handlers import ler_arquivo
from collections import deque
from pathlib import Path
from os import mkdir, getcwd
from numpy import random
from time import time
from functools import reduce

# Auxiliar da questão 1
def distancia_e_caminho_minimo(
    grafo: VetorAdj, vertices_finais: List[int]
) -> List[Tuple[int, Any]]:

    vertice_inicial = 10

    distancias, pais, S = dijkstra_com_vetor(grafo, vertice_inicial)

    conjunto_dist_e_min = []

    for fim in vertices_finais:
        print(f"calculando até {fim}")
        # Distância
        dist = distancias[fim - 1]

        # Reconstruindo caminho mínimo
        caminho_minimo = deque()

        #   construindo o vértice
        fim = Vertice(fim, dist)
        fim.pai = pais[fim.valor - 1]

        caminho_minimo.append(fim)

        pai = fim.pai

        while pai != -1:  # Denota que chegamos à raiz

            valor = pai
            peso_acumulado = distancias[pai - 1]

            vertice = Vertice(valor, peso_acumulado)

            pai = pais[valor - 1]
            vertice.pai = pai

            caminho_minimo.appendleft(vertice)

        conjunto_dist_e_min.append((dist, caminho_minimo))

    return conjunto_dist_e_min


def questao1(num_grafo: int, caminho_main: str) -> None:

    print(f"Grafo {num_grafo}")
    # Caminho de outputs
    output_path = Path(caminho_main.parents[0], "outputs")

    try:
        mkdir(output_path)
    except FileExistsError:
        pass

        n, arestas = ler_arquivo(
            Path(caminho_main / f"grafo_W_{num_grafo}_1.txt"),
            tem_pesos=True,
        )

        grafo = VetorAdj(n, arestas, tem_pesos=True)

    vertices_finais = [20, 30, 40, 50, 60]
    # Chamada da Função que 'executa o enunciado'
    dist_e_caminhos = distancia_e_caminho_minimo(grafo, vertices_finais)

    with open(Path(output_path, f"graph_{num_grafo}_questao1.txt"), "a") as file:

        for i in range(len(vertices_finais)):
            file.write(f"Medindo do vértice 10 ao {vertices_finais[i]}: \n")
            file.write(f"Distância: " + "{0:.2f}".format(dist_e_caminhos[i][0]) + "\n")
            file.write("Caminho Mínimo: \n")
            print(f"Montando caminho mínimo...")
            for vertice in dist_e_caminhos[i][1]:
                file.write(str(vertice) + "\n")
            file.write("\n")
            print(f"TERMINEI do 10 ao {vertices_finais[i]}, no grafo {num_grafo}...")


def tempos_dijkstra(grafo: VetorAdj, k: int):

    vertices_iniciais = []
    tempos_vetor = []
    tempos_heap = []

    for i in range(k):
        num_aleatorio = random.randint(1, grafo.num_vertices + 1)
        vertices_iniciais.append(num_aleatorio)

    for index, s in enumerate(vertices_iniciais):

        # Somente para monitoramento em execução
        # print(f"Estamos no índice {index}...")

        # Tempos Vetor
        tempo_inicial_vetor = time()
        dijkstra_com_vetor(grafo, s)
        tempo_final_vetor = time()

        diff_tempo_vetor = tempo_final_vetor - tempo_inicial_vetor
        tempos_vetor.append(diff_tempo_vetor)
        print(f"Vetor: {diff_tempo_vetor}")

        # Tempos Heap
        tempo_inicial_heap = time()
        dijkstra_com_heap(grafo, s)
        tempo_final_heap = time()

        diff_tempo_heap = tempo_final_heap - tempo_inicial_heap
        tempos_heap.append(diff_tempo_heap)
        print(f"Heap: {diff_tempo_heap}")

    return tempos_vetor, tempos_heap


def questao2(caminho_main: str):

    output_path = Path(caminho_main.parents[0], "outputs")

    for i in range(1, 6):
        n, arestas = ler_arquivo(
            Path(caminho_main / f"grafo_W_{i}_1.txt"),
            tem_pesos=True,
        )

        grafo = VetorAdj(n, arestas, tem_pesos=True)

        print(f"Grafo {i}")
        tempos_vetor, tempos_heap = tempos_dijkstra(grafo, 5)

        medio_vetor = sum(tempos_vetor) / len(tempos_vetor)
        medio_heap = sum(tempos_heap) / len(tempos_heap)

        with open(Path(output_path, f"graph_{i}_questao2.txt"), "a") as file:

            file.write(f"TEMPOS: \n\n")

            # Vetor
            file.write(f"Tempos de Vetor: \n")
            for item in tempos_vetor:
                file.write(str(item) + ", ")
            file.write(f"\n\nTempo Médio de Vetor: {medio_vetor}\n\n")

            # Heap
            file.write(f"Tempos de Heap: \n")
            for item in tempos_heap:
                file.write(str(item) + ", ")
            file.write(f"\n\nTempo Médio de Heap: {medio_heap}\n")


###############################################################################################################
# TESTES
