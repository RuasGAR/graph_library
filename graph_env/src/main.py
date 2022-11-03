from estudos_de_caso.parte2 import questao1, questao2
from pathlib import Path
from os import getcwd


def __main__():

    caminho_grafos = Path(
        getcwd(), "graph_env", "src", "estudos_de_caso", "grafos_parte2", "inputs"
    )

    for num_grafo in range(1, 6):
        questao1(num_grafo, Path(getcwd(), caminho_grafos))

    questao2(caminho_grafos)


__main__()
