import sys

sys.path.insert(1, "C:/Users/gabri/Desktop/graph_library/graph_env/src")

from typing import Dict, List, Tuple, Any
from data_structures.search_vertex import Vertice
from data_structures.adjacency_vector import VetorAdj
from searches.ford_fulkerson import encontrar_caminho_e_gargalo, construir_residual
from file_utils.file_handlers import ler_arquivo
from collections import deque
from pathlib import Path
from os import mkdir, getcwd
from numpy import random
from time import time
import numpy as np


def ler_grafo(caminho_main: str, num_grafo: int) -> None:

    n, arestas = ler_arquivo(
        Path(caminho_main / f"grafo_rf_{num_grafo}.txt"),
        tem_pesos=True,
        tipo_peso=np.int32,
    )

    vetor_adj = VetorAdj.formato_com_fluxo(n, arestas)

    return vetor_adj


########## TESTES ##########
grafo_em_vetor = ler_grafo(
    Path(getcwd(), "graph_env/src/estudos_de_caso/grafos_parte3/inputs"), 1
)

# Caminho Mínimo
caminho_min, gargalo = encontrar_caminho_e_gargalo(grafo_em_vetor, 1, 5)
print(f"Caminho Mínimo: {caminho_min}")
print(f"Gargalo: {gargalo}")

# Construção de Grafo Residual
grafo_residual = construir_residual(grafo_original=grafo_em_vetor)
grafo_residual.imprimir()
