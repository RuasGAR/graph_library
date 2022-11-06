import sys

sys.path.insert(1, "C:/Users/gabri/Desktop/graph_library/graph_env/src")

from typing import Dict, List, Tuple, Any
from data_structures.search_vertex import Vertice
from data_structures.adjacency_vector import VetorAdj
from searches.dijkstra import dijkstra_com_heap, dijkstra_com_vetor, mst
from file_utils.file_handlers import ler_arquivo
from collections import deque
from pathlib import Path
from os import mkdir
from numpy import random
from time import time
import numpy as np

####################### QUESTÕES #########################################


def questao1(caminho_main: str) -> None:

    # Caminho de outputs
    output_path = Path(caminho_main.parents[0], "outputs")
    vertices_finais = [20, 30, 40, 50, 60]

    for num_grafo in range(1, 6):
        grafo = ler_grafo(caminho_main, num_grafo=num_grafo)
        # Chamada da Função que 'executa o enunciado'
        dist_e_caminhos = distancia_e_caminho_minimo(grafo, vertices_finais)

        print(f"Grafo {num_grafo}")

        with open(Path(output_path, f"graph_{num_grafo}_Q1.txt"), "a") as file:

            for i in range(len(vertices_finais)):
                file.write(f"Medindo do vértice 10 ao {vertices_finais[i]}: \n")
                file.write(
                    f"Distância: " + "{0:.2f}".format(dist_e_caminhos[i][0]) + "\n"
                )
                file.write("Caminho Mínimo: \n")
                print(f"Montando caminho mínimo...")
                for vertice in dist_e_caminhos[i][1]:
                    file.write(str(vertice) + "\n")
                file.write("\n")
                print(
                    f"TERMINEI do 10 ao {vertices_finais[i]}, no grafo {num_grafo}..."
                )


def questao2(caminho_main: str):

    output_path = Path(caminho_main.parents[0], "outputs")

    for i in range(1, 6):

        grafo = ler_grafo(caminho_main, num_grafo=i)

        print(f"Grafo {i}")
        tempos_vetor, tempos_heap = tempos_dijkstra(grafo, 5)

        medio_vetor = sum(tempos_vetor) / len(tempos_vetor)
        medio_heap = sum(tempos_heap) / len(tempos_heap)

        with open(Path(output_path, f"graph_{i}_Q2.txt"), "a") as file:

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


def questao3(caminho_main: str) -> None:

    output_path = Path(caminho_main.parents[0], "outputs")
    vertice_inicial = 1

    for i in range(1, 6):

        grafo = ler_grafo(caminho_main, num_grafo=i)

        arvore_ger_minima = mst(grafo, vertice_inicial)
        custo_total = np.float64(sum(v.valor for v in arvore_ger_minima))

        with open(Path(output_path, f"grafo_W_{i}_Q3.txt"), "a") as file:
            file.write("Esta é a árvore geradora mínima encontrada no grafo: \n\n")
            file.write(f"A árvore tem o custo total de {custo_total}\n")
            file.write(f"A árvore geradora mínima está descrita logo abaixo:\n\n")
            for vertice in arvore_ger_minima:
                file.write(str(vertice) + "\n")
            file.write("FINAL\n\n")


############# Funções intermediárias de montagem ##############################
def distancia_e_caminho_minimo(
    grafo: VetorAdj, vertices_finais: List[int]
) -> List[Tuple[int, Any]]:

    vertice_inicial = np.int32(10)
    vertices = dijkstra_com_heap(grafo, vertice_inicial)

    todas_distancias_cam_min = []

    for fim in vertices_finais:
        caminho_min = construir_caminho_min(vertices, fim)
        dist = caminho_min[-1].peso
        todas_distancias_cam_min.append((dist, caminho_min))

    return todas_distancias_cam_min


def tempos_dijkstra(grafo: VetorAdj, k: int):

    vertices_iniciais = []
    tempos_vetor = []
    tempos_heap = []

    for i in range(k):
        num_aleatorio = random.randint(1, grafo.num_vertices + 1)
        vertices_iniciais.append(num_aleatorio)

    for index, s in enumerate(vertices_iniciais):

        # Somente para monitoramento em execução
        print(f"Estamos no índice {index}...")

        # Tempos Heap
        tempo_inicial_heap = time()
        dijkstra_com_heap(grafo, s)
        tempo_final_heap = time()

        diff_tempo_heap = tempo_final_heap - tempo_inicial_heap
        tempos_heap.append(diff_tempo_heap)
        print(f"Heap: {diff_tempo_heap}")

        # Tempos Vetor
        tempo_inicial_vetor = time()
        dijkstra_com_vetor(grafo, s)
        tempo_final_vetor = time()

        diff_tempo_vetor = tempo_final_vetor - tempo_inicial_vetor
        tempos_vetor.append(diff_tempo_vetor)
        print(f"Vetor: {diff_tempo_vetor}")

    return tempos_vetor, tempos_heap


##################### AUXILIARES ####################################################3


def ler_grafo(caminho_main: str, num_grafo: int):

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

    return grafo


def construir_caminho_min(vertices: List[Dict], fim: int) -> List[Vertice]:

    caminho_min = deque()
    v = vertices[fim - 1]
    prox = v.pai
    caminho_min.append(v)

    while prox != -1:
        prox_v = vertices[prox - 1]
        caminho_min.appendleft(prox_v)
        prox = prox_v.pai

    return caminho_min


###############################################################################################################
# TESTES
