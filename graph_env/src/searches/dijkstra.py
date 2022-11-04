import sys

sys.path.insert(1, "C:/Users/gabri/Desktop/graph_library/graph_env/src")
import numpy as np
from typing import Dict, List, Set, Tuple, Union
from data_structures.adjacency_vector import VetorAdj
from data_structures.search_vertex import Vertice
from file_utils.file_handlers import ler_arquivo
import heapdict


def dijkstra_com_vetor(grafo: VetorAdj, vertice_s: int) -> List[Dict]:

    vertices = [{}] * grafo.num_vertices
    distancias: List[Union[np.inf, np.int32]] = [
        np.float32(np.inf) for x in range(grafo.num_vertices)
    ]
    pais: List[int] = [np.int32(-1) for x in range(grafo.num_vertices)]

    conjunto_v: List[int] = set([np.int32(x) for x in range(1, grafo.num_vertices + 1)])
    conjunto_s: Set[int] = set([])

    distancias[vertice_s - 1] = np.float32(0)

    diferenca_de_conjuntos = set.difference(conjunto_v, conjunto_s)

    while len(diferenca_de_conjuntos) > 0:

        diferenca_conjuntos_lista = np.array(
            list(diferenca_de_conjuntos), dtype=np.int32
        )

        # Colhendo as distâncias elegíveis
        dist_na_diferenca = [distancias[x - 1] for x in diferenca_conjuntos_lista]
        indice_do_menor = np.argmin(dist_na_diferenca)

        u = np.int32(diferenca_conjuntos_lista[indice_do_menor])
        dist_u = np.float32(distancias[u - 1])

        # Adicionando ao conjunto e à lista de vértices
        conjunto_s.add(u)
        vertices[u - 1] = {
            "valor": u,
            "pai": pais[u - 1],
            "dist": dist_u,
        }

        for vizinho in grafo.percorrer_vizinhos(u):

            # Lembrando que um vizinho de u está armazenado numa tupla "(valor, peso_de_u_até_v)"
            valor_vizinho = vizinho[0]
            peso_u_vizinho = vizinho[1]

            indice_vizinho = valor_vizinho - 1

            if distancias[indice_vizinho] > dist_u + peso_u_vizinho:
                distancias[indice_vizinho] = dist_u + peso_u_vizinho
                pais[indice_vizinho] = u

        diferenca_de_conjuntos = set.difference(conjunto_v, conjunto_s)

    return vertices


def dijkstra_com_heap(grafo: VetorAdj, vertice_s: int) -> List[Dict]:

    vertices = [{}] * grafo.num_vertices

    distancias = heapdict.heapdict()
    pais: List[int] = [np.int32(-1) for x in range(grafo.num_vertices)]

    # Populando a heap
    for i in range(1, grafo.num_vertices + 1):
        distancias[np.int32(i)] = np.inf

    # Zerando a distância
    distancias[vertice_s] = np.float32(0)

    conjunto_v: List[int] = set([np.int32(x) for x in range(1, grafo.num_vertices + 1)])
    conjunto_s: Set[int] = set([])

    diferenca_de_conjuntos = set.difference(conjunto_v, conjunto_s)

    while len(diferenca_de_conjuntos) != 0:

        u, dist_u = distancias.popitem()

        # Adicionando ao conjunto de explorados (tanto conjunto_s, que contém só os valores)
        # como o vértice como um todo - em formato de dicionário - numa lista de vértices
        conjunto_s.add(u)
        vertices[u - 1] = {"valor": u, "pai": pais[u - 1], "dist": dist_u}

        for vizinho in grafo.percorrer_vizinhos(u):

            valor_vizinho = vizinho[0]
            peso_u_vizinho = vizinho[1]

            try:
                if distancias[valor_vizinho] > dist_u + peso_u_vizinho:
                    distancias[valor_vizinho] = np.float32(dist_u + peso_u_vizinho)
                    pais[valor_vizinho - 1] = u
            except KeyError:
                continue

        diferenca_de_conjuntos = set.difference(conjunto_v, conjunto_s)

    return vertices


###############################################################################################################
# TESTES

# 1) Dijkstra com vetor de pesos
""" n, arestas = ler_arquivo(
    "graph_env/src/searches/graph_teste_pesos_sem_negativo.txt", tem_pesos=True
)
grafo_em_vetor = VetorAdj(n, arestas, tem_pesos=True)

vertices = dijkstra_com_vetor(grafo_em_vetor, 1)

for item in vertices:
    vertice = Vertice(item["valor"], item["pai"], peso=item["dist"])
    print(vertice) """


# 2) Dijkstra com heap
""" n, arestas = ler_arquivo(
    "graph_env/src/searches/graph_teste_pesos_sem_negativo.txt", tem_pesos=True
)
grafo_em_vetor = VetorAdj(n, arestas, tem_pesos=True)

vertices = dijkstra_com_heap(grafo_em_vetor, 1)

for item in vertices:
    vertice = Vertice(item["valor"], item["pai"], peso=item["dist"])
    print(vertice) """
