# from estudos_de_caso.parte2 import questao1, questao2, questao3, questao4
from estudos_de_caso.parte3 import questao
from pathlib import Path
from os import getcwd


def __main__():

    caminho_grafos = Path(
        getcwd(), "graph_env", "src", "estudos_de_caso", "grafos_parte3", "inputs"
    )

    questao(caminho_grafos)


__main__()
