import sys

sys.path.insert(1, "C:/Users/gabri/Desktop/graph_library/graph_env/src")
import numpy as np
from typing import Dict, List, Set, Tuple, Union
from data_structures.adjacency_vector import VetorAdj
from data_structures.search_vertex import Vertice
from file_utils.file_handlers import ler_arquivo
import heapdict


def dijkstra_com_vetor(grafo: VetorAdj, vertice_s: int) -> List[Dict]:

    # Criação de vertices de todos os vértices, da fila de descobertos
    vertices: List[Dict] = [
        Vertice(x, -1, np.inf) for x in range(1, grafo.num_vertices + 1)
    ]

    # vai funcionar como se fosse uma fila, constantemente reordenada

    descobertos: List[Dict] = []

    # Setando distância do inicial e colocando-o entre os descobertos
    vertices[vertice_s - 1].peso = 0
    descobertos.append(vertices[vertice_s - 1])

    while len(descobertos) > 0:

        descobertos = sorted(descobertos, key=lambda x: x.peso)  # 0(n)

        # é o item com menor distância, já que há ordenação por este parâmetro
        u = descobertos.pop(0)
        u.marcador = True
        dist_u = u.peso

        for vizinho in grafo.percorrer_vizinhos(u.valor):

            # Lembrando que um vizinho de u está armazenado numa tupla "(valor, peso_de_u_até_v)"
            valor_vizinho = vizinho[0]
            peso_u_vizinho = vizinho[1]
            indice_vizinho = valor_vizinho - 1

            if vertices[indice_vizinho].marcador == True:
                continue

            if vertices[indice_vizinho].peso > dist_u + peso_u_vizinho:
                vertices[indice_vizinho].peso = dist_u + peso_u_vizinho
                vertices[indice_vizinho].pai = u.valor
                descobertos.append(vertices[indice_vizinho])

    return vertices


def dijkstra_com_heap(grafo: VetorAdj, vertice_s: int) -> List[Dict]:

    explorados = []

    distancias = heapdict.heapdict()
    # Populando a heap
    for i in range(1, grafo.num_vertices + 1):
        distancias[np.int32(i)] = np.inf
    pais: List[int] = [np.int32(-1) for x in range(grafo.num_vertices)]

    # Zerando a distância
    distancias[vertice_s] = np.float32(0)

    while bool(distancias) != False:

        u, dist_u = distancias.popitem()
        explorados.append(Vertice(u, pais[u - 1], dist_u))

        for vizinho in grafo.percorrer_vizinhos(u):

            valor_vizinho = vizinho[0]
            peso_u_vizinho = vizinho[1]

            try:
                if distancias[valor_vizinho] > dist_u + peso_u_vizinho:
                    distancias[valor_vizinho] = np.float32(dist_u + peso_u_vizinho)
                    pais[valor_vizinho - 1] = u
            except KeyError:
                continue
    return explorados


###############################################################################################################
# TESTES

# 1) Dijkstra com vetor de pesos
""" n, arestas = ler_arquivo(
    "graph_env/src/searches/graph_teste_pesos_sem_negativo.txt", tem_pesos=True
)
grafo_em_vetor = VetorAdj(n, arestas, tem_pesos=True)

vertices = dijkstra_com_vetor(grafo_em_vetor, 1)

for item in vertices:
    print(item) """


# 2) Dijkstra com heap
""" n, arestas = ler_arquivo(
    "graph_env/src/searches/graph_teste_pesos_sem_negativo.txt", tem_pesos=True
)
grafo_em_vetor = VetorAdj(n, arestas, tem_pesos=True)

vertices = dijkstra_com_heap(grafo_em_vetor, 1)

for item in vertices:
    print(item) """
