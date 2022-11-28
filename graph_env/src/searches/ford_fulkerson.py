# Primeiro, vamos precisar achar qualquer caminho entre s e t
# Aí, entramos no algoritmo de fato -> Talvez uma função auxiliar seja útil
# Começaremos o loop
# A princípio, não precisaremos de uma nova estrutura de dados. O vetor de adjacências direcionado é
# capaz de lidar com a construção do grafo residual.
# Porém, é interessante fazer um método só para isso também, nos quais podemos tratar o fluxo e a
# e a capacidade com modularidade.
# Como encontrar gargalos?

from typing import List
from data_structures.adjacency_vector import VetorAdj
import numpy as np


def ford_fulkerson(
    grafo: VetorAdj, fonte: np.int32, destino: np.int32, capacidade: np.int32
) -> np.int32:

    pass


def calcular_gargalo():
    pass


def construir_residual():

    caminho = encontrar_caminho()
    gargalo = calcular_gargalo()
    for v in caminho:
        # Se v é original: faz tal coisa
        #
        pass

    pass


def encontrar_caminho(partida: int, destino: int) -> List[int]:

    # Só vamos abstrair o uso da BFS aqui dentro
    pass
