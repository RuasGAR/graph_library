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
from data_structures.search_vertex import Vertice, Vertice_Residual
from searches.busca import Busca
from collections import deque
import numpy as np


def ford_fulkerson(
    grafo_original: VetorAdj, fonte: np.int32, destino: np.int32, capacidade: np.int32
) -> np.int32:

    # O grafo recebido é o grafo_original, que tem atributos de capacidade e etc
    # IMPORTANTE: os grafos nesse formato já vêm "inicializados" com fluxo inicial igual a 0
    grafo_residual = construir_residual(grafo_original)

    caminho_min, gargalo = encontrar_caminho_e_gargalo(grafo_original, fonte, destino)
    if caminho_min == None:
        return "Não é possível estabelecer um caminho mínimo entre a fonte e o destino especificados."
    # Aumento de fluxo

    pass


def aumentar_fluxo(grafo: VetorAdj, gargalo: int):
    pass


def construir_residual(grafo_original: VetorAdj):
    # Para esse grafo, como o que importa é o peso(capacidade), podemos usar a implementação anterior,
    # que foi estendida para poder ser direcionado ou não.

    n = grafo_original.num_vertices
    arestas_originais = grafo_original.arestas
    arestas_residuais: List[Tuple[int]] = []

    # Agora vem a parte "diferente": criar as arestas que "voltam"
    for aresta in arestas_originais:
        v1: Tuple[int] = aresta[0]
        v2: Tuple[int] = aresta[1]
        capacidade = aresta[2]
        fluxo_passante = aresta[3]
        original = True

        # Constrói a relação de capacidade e fluxo passante com as arestas originais ou não
        are_original = (v1, v2, capacidade - fluxo_passante, original)
        are_reversa = (v2, v1, fluxo_passante, not original)

        # Adiciona nas arestas residuais
        arestas_residuais.append(are_original)
        arestas_residuais.append(are_reversa)

    grafo_residual: VetorAdj = VetorAdj.formato_residual(
        num_vertices=n, arestas=arestas_residuais
    )

    return grafo_residual


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

    busca_em_grafo = Busca(grafo, e_residual=True)
    busca_em_grafo.bfs(
        Vertice(partida)
    )  # só chamada da função para alterar os nós marcados e sem ocupar mem
    resultado = busca_em_grafo.vertices

    # Construção do Caminho Mínimo

    # Ao invés de guardar uma lista de vértices, vamos passar só uma tupla com vértices e seus pais
    # O objetivo é tentar entender o quanto a classe Vertice tem influenciado no tempo de execução dos
    # algoritmos - em especial, a construção do formato utilizado na mesma função do algoritmo em si.

    caminho_min = deque()  # type hint seria algo como List[Tuple[int]]
    destino: Vertice_Residual = resultado[destino - 1]
    gargalo: int = destino.peso

    while destino.pai != None:

        # Checando a capacidade mínima
        destino.peso = np.int32(destino.peso)  # capacidades são inteiras
        if destino.peso < gargalo:
            gargalo = destino.peso

        # Parte de construção da 3-upla de caminho
        indice_pai = destino.pai - 1
        caminho_min.appendleft(
            (destino.valor, destino.pai, destino.peso, destino.original_ou_reversa)
        )
        destino = resultado[indice_pai]

    # Inclusão da raiz
    caminho_min.appendleft(
        (
            destino.valor,
            destino.pai,
            np.int32(destino.peso),
            destino.original_ou_reversa,
        )
    )

    if len(caminho_min) == 1:
        # Se só tiver a raiz, é como não ter caminho
        return None

    return (caminho_min, gargalo)


########## TESTES

# Serão feitos diretamente no arquivo parte 3, em 'graph_env/src/estudos_de_caso'
# Ainn testes automatizaduuus, cadê você
