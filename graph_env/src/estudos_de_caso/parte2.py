import sys

sys.path.insert(1, "C:/Users/gabri/Desktop/graph_library/graph_env/src")

from typing import List, Tuple
from data_structures.search_vertex import Vertice
from data_structures.adjacency_vector import VetorAdj
from searches.dijkstra import dijkstra_com_heap, dijkstra_com_vetor
from file_utils.file_handlers import ler_arquivo
from collections import deque
from pathlib import Path
from os import mkdir, getcwd


def distancia_e_caminho_minimo(grafo: VetorAdj, vertice_final: int) -> Tuple[int, List]:

    vertice_inicial = 10

    distancias, pais, S = dijkstra_com_vetor(grafo, vertice_inicial)
    # [1,2,3,4,5]
    # [5,4,3,2,1]
    # [2,4,5,3,6]

    # Distância
    dist = distancias[vertice_final - 1]

    # Reconstruindo caminho mínimo
    caminho_minimo = deque()

    #   construindo o vértice
    vertice_final = Vertice(vertice_final, dist)
    vertice_final.pai = pais[vertice_final.valor - 1]

    caminho_minimo.append(vertice_final)

    pai = vertice_final.pai

    while pai != -1:  # Denota que chegamos à raiz

        valor = pai
        peso_acumulado = distancias[pai - 1]

        vertice = Vertice(valor, peso_acumulado)

        pai = pais[valor - 1]
        vertice.pai = pai

        caminho_minimo.appendleft(vertice)

    return (dist, caminho_minimo)


def questao1(fim: int, caminho_main: str) -> None:

    # Caminho de outputs
    output_path = Path(caminho_main.parents[0], "outputs")

    try:
        mkdir(output_path)
    except FileExistsError:
        pass

    for i in range(1, 6):

        n, arestas = ler_arquivo(
            Path(caminho_main / f"grafo_W_{i}_1.txt"),
            tem_pesos=True,
        )

        grafo = VetorAdj(n, arestas, tem_pesos=True)

        # Chamada da Função que 'executa o enunciado'
        dist, caminho_minimo = distancia_e_caminho_minimo(grafo, fim)

        with open(Path(output_path, f"graph_{i}_questao1.txt"), "a") as file:
            file.write(f"Medindo do vértice 10 ao {fim}: \n")
            file.write(f"Distância: " + "{0:.2f}".format(dist) + "\n")
            file.write("Caminho Mínimo: \n")
            for vertice in caminho_minimo:
                file.write(str(vertice) + "\n")
            file.write("\n")


###############################################################################################################
# TESTES
