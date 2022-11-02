import sys

# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, "C:/Users/gabri/Desktop/graph_library/graph_env/src")

import numpy as np
from typing import List, Set, Tuple, Union
from data_structures.adjacency_vector import VetorAdj
from data_structures.search_vertex import Vertice
from file_utils.file_handlers import ler_arquivo


def dijkstra_com_vetor(
    grafo: VetorAdj, vertice_s: int
) -> Tuple[List[int], List[Vertice]]:

    distancias: List[Union[np.inf, np.int32]] = [
        np.float32(np.inf) for x in range(grafo.num_vertices)
    ]
    pais: List[int] = [np.int32(-1) for x in range(grafo.num_vertices)]

    conjunto_v: List[int] = set(map(lambda element: element.valor, grafo.container))
    conjunto_s: Set[int] = set([])

    distancias[vertice_s - 1] = np.float32(0)

    diferenca_de_conjuntos = conjunto_v - conjunto_s

    while len(diferenca_de_conjuntos) != 0:

        diferenca_de_conjuntos = conjunto_v - conjunto_s

        if len(diferenca_de_conjuntos) == 0:
            u = vertice_s
            dist_u = 0
        else:
            diferenca_conjuntos_lista = np.array(
                list(diferenca_de_conjuntos), dtype=np.int32
            )

            try:
                indice_do_menor = np.argmin(diferenca_conjuntos_lista)
            except ValueError:
                indice_do_menor = 0

            u = diferenca_conjuntos_lista[indice_do_menor]
            dist_u = distancias[u - 1]
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

    pass


def mst():
    pass


###############################################################################################################
# TESTES

# 1) Dijkstra com vetor de pesos
n, arestas = ler_arquivo(
    "graph_env/src/searches/graph_teste_pesos_sem_negativo.txt", tem_pesos=True
)
grafo_em_vetor = VetorAdj(n, arestas, tem_pesos=True)

distancias, pais, s = dijkstra_com_vetor(grafo_em_vetor, 1)

for item in s:
    vertice = Vertice(item, distancias[item - 1])
    vertice.pai = pais[item - 1]
    print(vertice)
