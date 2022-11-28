from typing import List, Union
import sys

# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, "/home/ruasgar/Bureau/trabalho_grafos/graph_env/src")

from file_utils.file_handlers import ler_arquivo
from data_structures.adjacency_vector import VetorAdj
from data_structures.adjacency_matrix import MatrizAdj
from data_structures.search_vertex import Vertice
from collections import deque
import numpy as np


class Busca:
    def __init__(self, grafo: Union[MatrizAdj, VetorAdj]) -> None:
        self.grafo: Union[MatrizAdj, VetorAdj] = grafo
        self.vertices: List[Vertice] = []

        if isinstance(grafo, VetorAdj):
            self.vertices = [
                Vertice(x.valor) for x in grafo.container
            ]  # Quantidade de elementos no vetor container é n
        elif isinstance(grafo, MatrizAdj):
            self.vertices = [
                Vertice(x + 1) for x in range(len(grafo.matriz))
            ]  # Quantidade de linhas da matriz é n

    def bfs(self, vertice_s: Vertice) -> List[Vertice]:

        # Desmarcar todos os vértices
        # Por natureza, já são desmarcados, mas alterando por referência, é sempre bom rever

        for no in self.vertices:
            no.marcador = False
            no.pai = None
            no.nivel = 0

        # Setar fila Q
        fila = deque()

        # Marcar s, denotar seu nível, e inserir na fila
        self.vertices[vertice_s.valor - 1].marcador = True
        # vertice_s.nivel = 0; desnecessário, mas vou deixar o comentário pra lembrar
        fila.append(vertice_s)

        # Loop
        while len(fila) != 0:

            v = fila.pop()

            for w in self.grafo.percorrer_vizinhos(v.valor):

                vizinho_no_vetor: Vertice = self.vertices[w - 1]

                if vizinho_no_vetor.marcador == False:
                    vizinho_no_vetor.marcador = True
                    vizinho_no_vetor.nivel = v.nivel + 1
                    vizinho_no_vetor.pai = v.valor
                    # o ideal seria o endereço de v, mas...

                    fila.insert(0, vizinho_no_vetor)

        return list(filter(lambda x: x.marcador == True, self.vertices))

    def dfs(self, vertice_s: Vertice) -> List[Vertice]:
        # dermarcando todos os vértices
        for no in self.vertices:
            no.marcador = False
            no.pai = None
            no.nivel = 0

        # pegar no vetor de vértices o vértice s
        pilha = deque()

        pilha.append(self.vertices[vertice_s.valor - 1])

        while len(pilha) != 0:

            u: Vertice = pilha.popleft()

            if u.marcador == False:
                # O elemento que está na posição relativa do vértice retirado dentro de vetor de vértices (self.vertices)
                u_no_vetor = self.vertices[u.valor - 1]
                # Mesma ideia: precisamos marcar o vértice no vetor self.vertices; por isso não pegamos somente o vérice U isolado
                u_no_vetor.marcador = True

                # Vamos pegar os vizinhos e se for uma matriz de adj, precisamos inverter sua ordem:
                vizinhos_de_u: List[int] = self.grafo.percorrer_vizinhos(
                    u_no_vetor.valor
                )
                if isinstance(self.grafo, MatrizAdj):
                    vizinhos_de_u.reverse()

                # percorremos os vizinhos
                for vizinho in vizinhos_de_u:
                    vizinho_no_vetor = self.vertices[vizinho - 1]

                    if vizinho_no_vetor.marcador == False:
                        vizinho_no_vetor.pai = u_no_vetor.valor
                        vizinho_no_vetor.nivel = u_no_vetor.nivel + 1
                    pilha.insert(0, vizinho_no_vetor)

        return list(filter(lambda x: x.marcador == True, self.vertices))

    def _pegar_menor_dist(distancias: List[int]):

        menor = distancias[0]
        indice_do_menor = 0
        for i in range(1, len(distancias)):
            if distancias[i] < menor:
                menor = distancias[i]
                indice_do_menor = i

        return menor, indice_do_menor


# n, arestas = ler_arquivo("graph_env/src/searches/8_vertex_graph.txt")


""" Testes para matriz de adjacência """

# grafo_em_matriz = MatrizAdj(n);
# grafo_em_matriz.inserir_arestas(arestas);
# grafo_em_matriz.mostra_matriz();
# print(grafo_em_matriz.percorrer_vizinhos(3));
# matriz_busca = Busca(grafo_em_matriz);

# Teste na BFS
# print(matriz_busca.bfs(Vertice(5)),'\n')
# print(matriz_busca.bfs(Vertice(1)),'\n')

# Teste na DFS
# print(matriz_busca.dfs(Vertice(4)),'\n')
# print(matriz_busca.dfs(Vertice(2)),'\n')


""" Testes para vetor de adjacências """

# grafo_em_vetor = VetorAdj.formato_tradicional(n, arestas);
# vetor_adj_busca = Busca(grafo_em_vetor);
# print(str(vetor_adj_busca.vertices)[1:-1].replace(', ',''));

# Teste na BFS
# Ordem é ligeramente diferente por conta da ordem de leitura das arestas e sua consequente inserção nos vetores de vizinhos.
# print(vetor_adj_busca.bfs(Vertice(1)));

# Teste na DFS
# print(vetor_adj_busca.dfs(Vertice(4)));
