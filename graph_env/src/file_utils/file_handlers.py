from typing import List, Tuple
from os import path, getcwd
from numpy import int32


def ler_arquivo(caminho: str) -> None:
    numero_vertices: int
    arestas: List[Tuple(int)] = []

    with open(path.join(getcwd(), caminho), 'r') as file:
        linhas = file.readlines()
        numero_vertices = int(linhas[0])
        for linha in linhas[1:]:
            numeros_na_linha = linha.split(' ')  # separa por backspace
            aresta = (int32(numeros_na_linha[0]), int32(numeros_na_linha[1]))
            # adiciona tupla da aresta na lista de arestas
            arestas.append(aresta)

    return [numero_vertices, arestas]


#caminho = 'test.txt';

#numerozin, arestaszinhas = ler_arquivo(caminho);

# print(f"Vértices:{numerozin}");
# print(f"Arestas:{arestaszinhas}");
