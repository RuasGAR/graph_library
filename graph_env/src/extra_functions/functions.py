from typing import List, Union

import sys

import numpy as np
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

def distancia(grafo:Union[MatrizAdj, VetorAdj], origem:Vertice, destino:Vertice) -> Union[Vertice, None]:

    explorados:List[Vertice] = Busca(grafo).bfs(origem);
    
    if(explorados[origem.valor-1] and explorados[destino.valor-1]):
        return (explorados[destino.valor-1].nivel - explorados[origem.valor-1].nivel)
    
    return None;

def diametro(grafo:Union[MatrizAdj, VetorAdj]) -> int:

    # Tem que chamar a função de distância para cada combinação de vértices
    # Dá pra ser feito com dois loops. Atualizar a maior se for necessária.

    diametro:int = 0;
    for i in range(grafo.num_vertices):
        for j in range(grafo.num_vertices):
            nova_distancia = distancia(grafo, Vertice(i), Vertice(j));
            if(nova_distancia > diametro):
                diametro = nova_distancia;
    return diametro

def componentes_conexas(grafo:Union[MatrizAdj, VetorAdj]) -> List[object[List[Vertice],int]]:
    
    # Estruturas auxiliares
        # Lista de componentes conexas
        # Dicionário relacionando cada uma das componentes ao seu respectivo tamanho

    componentes_conexas:List[object[List[Vertice],int]] = [];

    # Instância da busca, para que tenhamos os vértices com as marcações e possamos, intuitivamente, realizar as buscas
    busca_em_grafo:Busca = Busca(grafo);
    
    """ primeira_componente = busca_em_grafo.bfs(busca_em_grafo.vertices[0]);
    
    # Atualizamos os dados do objeto do primeiro componente na lista
    componentes_conexas[0]["valor"] = primeira_componente;
    componentes_conexas[0]["tamanho"] = len(primeira_componente); """


    # O(n) e dobra o custo de memória
    # Porém, removemos as referências para os vértices "originais" e não precisamos nos preocupar em alterá-los diretamente
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

n, arestas = ler_arquivo("graph_env/src/8_vertex_graph.txt")


# Testes para matriz de adjacência

#grafo_em_matriz = MatrizAdj(n);
#grafo_em_matriz.inserir_arestas(arestas);
""" print(f"Max: {grau_maximo(grafo_em_matriz)}\n");
print(f"Min: {grau_minimo(grafo_em_matriz)}\n");
print(f"Médio: {grau_medio(grafo_em_matriz)}\n");
print(f"Mediana: {grau_mediana(grafo_em_matriz)}\n");
print(f"Distância entre 4 e 1: {distancia(grafo_em_matriz,Vertice(4),Vertice(1))}")
print(f"Diâmetro: {diametro(grafo_em_matriz)}"); """
#print(f"Componentes Conexas: {componentes_conexas(grafo_em_matriz)}");

# Testes para vetor de adjacências

""" grafo_em_vetor = VetorAdj(n, arestas);
#print(str(vetor_adj_busca.vertices)[1:-1].replace(', ','')); #print chatinho pra kct
print(f"\nMax: {grau_maximo(grafo_em_vetor)}\n");
print(f"Min: {grau_minimo(grafo_em_vetor)}\n");
print(f"Médio: {grau_medio(grafo_em_vetor)}\n");
print(f"Mediana: {grau_mediana(grafo_em_vetor)}\n");
print(f"Distância entre 3 e 1: {distancia(grafo_em_vetor,Vertice(3),Vertice(1))}\n")
print(f"Diâmetro: {diametro(grafo_em_vetor)}") """

