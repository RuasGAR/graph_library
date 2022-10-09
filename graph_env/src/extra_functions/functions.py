from timeit import timeit
from typing import List, Mapping, Union

import sys

import numpy as np
from math import inf, isinf

# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1,'/home/ruasgar/Bureau/trabalho_grafos/graph_env/src');

from data_structures.adjacency_vector import VetorAdj
from data_structures.adjacency_matrix import MatrizAdj
from data_structures.search_vertex import Vertice
from searches.busca import Busca
from file_utils.file_handlers import ler_arquivo
from copy import deepcopy


def grau_maximo(grafo:Union[MatrizAdj, VetorAdj]) -> int:
    return grafo.grau_maximo();

def grau_minimo(grafo:Union[MatrizAdj, VetorAdj]) -> int:
    return grafo.grau_minimo();

def grau_medio(grafo:Union[MatrizAdj, VetorAdj]) -> np.float32:
    return grafo.grau_medio();

def grau_mediana(grafo:Union[MatrizAdj, VetorAdj]) -> int:
    return grafo.grau_mediana();

def distancia(grafo:Union[MatrizAdj, VetorAdj], origem:int, destino:int) -> Union[int,float]:

    if(origem == destino):
        return inf;

    explorados:List[Vertice] = Busca(grafo).bfs(Vertice(origem));

    # Verificar se o vertice de destino está nos alcançaveis a partir da origem.
    # Não podemmos verificar pela estrutura do vértice, e sim pelo seu valor.
    # Para casos de desconexão, retornamos infinito 
    
    nivel_vertice_final:int = 0;

    for vertice in explorados:
        if(vertice.valor == destino):
            nivel_vertice_final = vertice.nivel;
    
    # Checamos se o final foi encontrado; se não, os dois vértices não tem conectividade, e portanto, sua distância é infinita
    if(nivel_vertice_final != 0):
        return nivel_vertice_final;
    
    return inf;

def diametro(grafo:Union[MatrizAdj, VetorAdj]) -> int:

    # Tem que chamar a função de distância para cada combinação de vértices
    # Dá pra ser feito com dois loops. Atualizar a maior se for necessária.

    diametro:int = 0;
    for i in range(grafo.num_vertices):
        for j in range(i+1,grafo.num_vertices):
            nova_distancia = distancia(grafo, i+1,j);
            if(isinf(nova_distancia) == False and nova_distancia > diametro):
                diametro = nova_distancia;
    return diametro

def componentes_conexas(grafo:Union[MatrizAdj, VetorAdj]) -> List[Mapping[List[Vertice],int]]:
    
    # Estruturas auxiliares
        # Lista de componentes conexas
        # Dicionário relacionando cada uma das componentes ao seu respectivo tamanho

    componentes_conexas:List[Mapping[List[Vertice],int]] = [];

    # Instância da busca, para que tenhamos os vértices com as marcações e possamos, intuitivamente, realizar as buscas
    busca_em_grafo:Busca = Busca(grafo);


    # O(n) e dobra o custo de memória
    # Além disso, nesse formato, adotamos uma abordagem que leva o maior custo no início do algoritmo, e vai aliviando
    # espaço conforme as componentes forem descobertas
    desmarcados:List[Vertice] = list(map(lambda v: v.valor,deepcopy(busca_em_grafo.vertices)));  

    while (len(desmarcados) > 0): # Checagem 0(1)
        
        # pega componente
        componente:List[Vertice] = busca_em_grafo.bfs(Vertice(desmarcados[0]));    
        
        # Componentes serão armazenadas no formato deste objeto
        componentes_conexas.append({"valor":componente, "tamanho":len(componente)});
        
        # remove os vertices da cópia que forem marcados
        for vertice in componente: # c vertices
            if(vertice.valor in desmarcados): # n VAI CAINDO
                try:
                    del desmarcados[desmarcados.index(vertice.valor)]; n 
                except:
                    continue
    
    # Ordenar componentes pelo seu tamanho (de forma descrescente)
    componentes_conexas.sort(key=lambda componente: componente["tamanho"], reverse=True);

    return componentes_conexas;



###### TEST ZONE !!!! ########################################

#n, arestas = ler_arquivo("graph_env/src/examples/8_vertex_graph.txt")

# Testes para matriz de adjacência

#grafo_em_matriz = MatrizAdj(n);
#grafo_em_matriz.inserir_arestas(arestas);
""" print(f"Max: {grau_maximo(grafo_em_matriz)}\n");
print(f"Min: {grau_minimo(grafo_em_matriz)}\n");
print(f"Médio: {grau_medio(grafo_em_matriz)}\n");
print(f"Mediana: {grau_mediana(grafo_em_matriz)}\n");
print(f"Distância entre 4 e 1: {distancia(grafo_em_matriz,4,1)}")
#print(f"Componentes Conexas: {componentes_conexas(grafo_em_matriz)}"); """
#print(f"Diâmetro: {diametro(grafo_em_matriz)}\n"); 
#print(f"Distância entre 8 e 4: {distancia(grafo_em_matriz,8,4)}")


# Testes para vetor de adjacências

#grafo_em_vetor = VetorAdj(n, arestas);

#print(str(vetor_adj_busca.vertices)[1:-1].replace(', ',''));
#print(f"\nMax: {grau_maximo(grafo_em_vetor)}\n");
#print(f"Min: {grau_minimo(grafo_em_vetor)}\n");
#print(f"Médio: {grau_medio(grafo_em_vetor)}\n");
#print(f"Mediana: {grau_mediana(grafo_em_vetor)}\n");
#print(f"Distância entre 9 e 11: {distancia(grafo_em_vetor,9,11)}\n")
#print(f"Diâmetro: {diametro(grafo_em_vetor)}\n")
#print(f"Componentes Conexas: {componentes_conexas(grafo_em_vetor)}");

