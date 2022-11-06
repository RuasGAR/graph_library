from estudos_de_caso.parte2 import questao1, questao2, questao3
from pathlib import Path
from os import getcwd


def __main__():

    caminho_grafos = Path(
        getcwd(), "graph_env", "src", "estudos_de_caso", "grafos_parte2", "inputs"
    )

    # questao1(caminho_grafos)

    # questao2(caminho_grafos)

    questao3(caminho_grafos)


__main__()
