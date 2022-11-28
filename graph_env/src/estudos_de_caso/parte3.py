import sys

sys.path.insert(1, "C:/Users/gabri/Desktop/graph_library/graph_env/src")

from typing import Dict, List, Tuple, Any
from data_structures.search_vertex import Vertice
from data_structures.adjacency_vector import VetorAdj
from searches.dijkstra import dijkstra_com_heap, dijkstra_com_vetor, mst
from file_utils.file_handlers import ler_arquivo
from collections import deque
from pathlib import Path
from os import mkdir, getcwd
from numpy import random
from time import time
import numpy as np


def ler_grafo(caminho_main: str, num_grafo: int) -> None:

    n, arestas = ler_arquivo(
        Path(caminho_main / f"grafo_rf_{num_grafo}.txt"), tem_pesos=True
    )

    vetor_adj = VetorAdj.formato_tradicional(
        n, arestas, tem_pesos=True, direcionado=True
    )

    return vetor_adj


########## TESTES ##########
vetor = ler_grafo(
    Path(getcwd(), "graph_env/src/estudos_de_caso/grafos_parte3/inputs"), 1
)
