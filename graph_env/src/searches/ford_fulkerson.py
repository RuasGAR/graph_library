# Primeiro, vamos precisar achar qualquer caminho entre s e t
# Aí, entramos no algoritmo de fato -> Talvez uma função auxiliar seja útil
# Começaremos o loop
# A princípio, não precisaremos de uma nova estrutura de dados. O vetor de adjacências direcionado é
# capaz de lidar com a construção do grafo residual.
# Porém, é interessante fazer um método só para isso também, nos quais podemos tratar o fluxo e a
# e a capacidade com modularidade.
# Como encontrar gargalos?

import sys

sys.path.insert(1, "C:/Users/gabri/Desktop/graph_library/graph_env/src")

from typing import List, Tuple
from data_structures.adjacency_vector import VetorAdj
from data_structures.search_vertex import Vertice
from searches.busca import Busca
from collections import deque
import numpy as np


def ford_fulkerson(
    grafo: VetorAdj, fonte: np.int32, destino: np.int32, capacidade: np.int32
) -> np.int32:

    caminho_min = encontrar_caminho(grafo, fonte, destino)
    if caminho_min == None:
        return "Não é possível estabelecer um caminho mínimo entre a fonte e o destino especificados."
    gargalo = calcular_gargalo(caminho_min)

    pass


def calcular_gargalo(caminho: List[Tuple[int]]) -> Tuple[int]:
    # Essa função recebe o caminho mínimo encontrado.
    # Deve retornar a aresta de menor capacidade neste caminho.

    # Aqui vamos pegar o item com a menor capacidade (o índice 2 de cada tripla de aresta)
    aresta_menor_capacidade = min(caminho, key=lambda aresta: aresta[2])

    return aresta_menor_capacidade


def construir_residual():

    caminho = encontrar_caminho()
    gargalo = calcular_gargalo()
    for v in caminho:
        # Se v é original: faz tal coisa
        #
        pass

    pass


def encontrar_caminho_e_gargalo(
    grafo: VetorAdj, partida: int, destino: int
) -> Tuple[List[Tuple[int]], int]:

    # Ao invés de usar o próprio retorno da BFS - que só contém a árvore formada,
    # com todos os nós que foram marcados - vamos pegar a lista inteira de vértices.
    # Isso vai facilitar muito a checagem de alcance, o que significa também a presença ou não
    # de caminho mínimo entre um vértice e outro.
    # Mais importante, ademais, é que isso permite a reconstrução do caminho mínimo de maneira
    # mais fácil, uma vez que essa parcela de memória já está alocada e salva.
    # Caso optássemos pelo retorno original da parte 1, teríamos um sério overhead de execução

    busca_em_grafo = Busca(grafo, tem_pesos=True)
    busca_em_grafo.bfs(
        Vertice(partida)
    )  # só chamada da função para alterar os nós marcados e sem ocupar mem
    resultado = busca_em_grafo.vertices

    # Construção do Caminho Mínimo

    # Ao invés de guardar uma lista de vértices, vamos passar só uma tupla com vértices e seus pais
    # O objetivo é tentar entender o quanto a classe Vertice tem influenciado no tempo de execução dos
    # algoritmos - em especial, a construção do formato utilizado na mesma função do algoritmo em si.

    caminho_min = deque()  # type hint seria algo como List[Tuple[int]]
    destino: Vertice = resultado[destino - 1]
    gargalo: int = destino.peso

    while destino.pai != None:

        # Checando a capacidade mínima
        destino.peso = np.int32(destino.peso)  # capacidades são inteiras
        if destino.peso < gargalo:
            gargalo = destino.peso

        # Parte de construção da 3-upla de caminho
        indice_pai = destino.pai - 1
        caminho_min.appendleft((destino.valor, destino.pai, destino.peso))
        destino = resultado[indice_pai]

    # Inclusão da raiz
    caminho_min.appendleft((destino.valor, destino.pai, np.int32(destino.peso)))

    if len(caminho_min) == 1:
        # Se só tiver a raiz, é como não ter caminho
        return None

    return (caminho_min, gargalo)


########## TESTES

# Serão feitos diretamente no arquivo parte 3, em 'graph_env/src/estudos_de_caso'
# Ainn testes automatizaduuus, cadê você
