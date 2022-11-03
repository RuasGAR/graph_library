from estudos_de_caso.parte2 import questao1, questao2
from pathlib import Path
from os import getcwd


def __main__():

    caminho_grafos = Path(
        getcwd(), "graph_env", "src", "estudos_de_caso", "grafos_parte2", "inputs"
    )

    for fim in [20, 30, 40, 50, 60]:
        questao1(fim, Path(getcwd(), caminho_grafos))

    questao2(caminho_grafos)


__main__()
