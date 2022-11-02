import sys

# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, "C:/Users/gabri/Desktop/graph_library/graph_env/src")

import numpy as np
from typing import List, Set, Tuple, Union
from data_structures.adjacency_vector import VetorAdj
from data_structures.search_vertex import Vertice
from file_utils.file_handlers import ler_arquivo
import heapdict


def dijkstra_com_vetor(
    grafo: VetorAdj, vertice_s: int
) -> Tuple[List[int], List[Vertice]]:

    distancias: List[Union[np.inf, np.int32]] = [
        np.float32(np.inf) for x in range(grafo.num_vertices)
    ]
    pais: List[int] = [np.int32(-1) for x in range(grafo.num_vertices)]

    conjunto_v: List[int] = set([np.int32(x) for x in range(1, grafo.num_vertices + 1)])
    conjunto_s: Set[int] = set([])

    distancias[vertice_s - 1] = np.float32(0)

    diferenca_de_conjuntos = conjunto_v - conjunto_s

    while len(diferenca_de_conjuntos) != np.int32(0):

        diferenca_de_conjuntos = conjunto_v - conjunto_s

        if len(diferenca_de_conjuntos) == 0:
            u = np.int32(vertice_s)
            dist_u = np.int32(0)
        else:
            diferenca_conjuntos_lista = np.array(
                list(diferenca_de_conjuntos), dtype=np.int32
            )

            try:
                indice_do_menor = np.argmin(diferenca_conjuntos_lista)
            except ValueError:
                indice_do_menor = 0

            u = np.int32(diferenca_conjuntos_lista[indice_do_menor])
            dist_u = np.float32(distancias[u - 1])
        # Fim do else
        conjunto_s.add(u)

        for vizinho in grafo.percorrer_vizinhos(u):

            # Lembrando que um vizinho de u está armazenado numa tupla "(valor, peso_de_u_até_v)"
            valor_vizinho = vizinho[0]
            peso_u_vizinho = vizinho[1]

            indice_vizinho = valor_vizinho - 1

            if distancias[indice_vizinho] > dist_u + peso_u_vizinho:
                distancias[indice_vizinho] = dist_u + peso_u_vizinho
                pais[indice_vizinho] = u

    return (distancias, pais, np.array(list(conjunto_s), dtype=np.int32))


def dijkstra_com_heap(
    grafo: VetorAdj, vertice_s: int
) -> Tuple[List[int], List[Vertice]]:

    # Dicionário que tem formato dict[valor] = prioridade; junto a métodos de heap e suporte à atualização de chaves
    distancias = heapdict.heapdict()
    pais: List[int] = [np.int32(-1) for x in range(grafo.num_vertices)]

    # Populando a heap #### consertar formatador do VSCODE pq tá triste isso"
    for i in range(1, grafo.num_vertices + 1):
        distancias[
            np.int32(i)
        ] = (
            np.inf
        )  # Inserção: seria de O(log n), mas nesse caso acho que depende do tamanho de alocação tabela

    distancias[vertice_s] = np.int32(0)

    conjunto_v: List[int] = set([np.int32(x) for x in range(1, grafo.num_vertices + 1)])
    conjunto_s: Set[int] = set([])

    diferenca_de_conjuntos = conjunto_v - conjunto_s

    while len(diferenca_de_conjuntos) != np.int32(0) and bool(
        distancias
    ):  # bool(distancias) verifica se heap está vazia

        diferenca_de_conjuntos = conjunto_v - conjunto_s

        u, dist_u = distancias.popitem()
        conjunto_s.add(u)

        for vizinho in grafo.percorrer_vizinhos(u):

            valor_vizinho = vizinho[0]
            peso_u_vizinho = vizinho[1]

            try:
                if distancias[valor_vizinho] > dist_u + peso_u_vizinho:
                    distancias[valor_vizinho] = np.float32(dist_u + peso_u_vizinho)
                    pais[valor_vizinho - 1] = u
            except KeyError:
                continue

    return (distancias, pais, np.array(list(conjunto_s), dtype=np.int32))


def mst():
    pass


###############################################################################################################
# TESTES

# 1) Dijkstra com vetor de pesos
""" n, arestas = ler_arquivo(
    "graph_env/src/searches/graph_teste_pesos_sem_negativo.txt", tem_pesos=True
)
grafo_em_vetor = VetorAdj(n, arestas, tem_pesos=True)

distancias, pais, s = dijkstra_com_vetor(grafo_em_vetor, 1)

for item in s:
    vertice = Vertice(item, distancias[item - 1])
    vertice.pai = pais[item - 1]
    print(vertice) """


# 2) Dijkstra com heap
""" n, arestas = ler_arquivo(
    "graph_env/src/searches/graph_teste_pesos_sem_negativo.txt", tem_pesos=True
)
grafo_em_vetor = VetorAdj(n, arestas, tem_pesos=True)

dijkstra_com_heap(grafo_em_vetor, 1)

distancias, pais, s = dijkstra_com_vetor(grafo_em_vetor, 1)

for item in s:
    vertice = Vertice(item, distancias[item - 1])
    vertice.pai = pais[item - 1]
    print(vertice) """
