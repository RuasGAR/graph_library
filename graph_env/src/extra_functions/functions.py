from asyncio.windows_utils import BUFSIZE
import sys
    # caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1,'/home/ruasgar/Bureau/trabalho_grafos/graph_env/src');

from data_structures.adjacency_vector import VetorAdj
from data_structures.adjacency_matrix import MatrizAdj
from data_structures.search_vertex import Vertice
from searches.busca import Busca
from file_utils.file_handlers import ler_arquivo
from copy import deepcopy


def grau_maximo(grafo):
    return grafo.grau_maximo();

def grau_minimo(grafo):
    return grafo.grau_minimo();

def grau_medio(grafo):
    return grafo.grau_medio();

def grau_mediana(grafo):
    return grafo.grau_mediana();

def distancia(grafo, origem, destino):

    explorados = Busca(grafo).bfs(origem);
    
    if(explorados[origem.valor-1] and explorados[destino.valor-1]):
        return (explorados[destino.valor-1].nivel - explorados[origem.valor-1].nivel)
    
    return None;

def diametro(grafo):

    # Tem que chamar a função de distância para cada combinação de vértices
    # Dá pra ser feito com dois loops. Atualizar a maior se for necessária.

    diametro = 0;
    for i in range(grafo.num_vertices):
        for j in range(grafo.num_vertices):
            nova_distancia = distancia(grafo, Vertice(i), Vertice(j));
            if(nova_distancia > diametro):
                diametro = nova_distancia;
    return diametro

def componentes_conexas(grafo):
    
    # Estruturas auxiliares
        # Lista de componentes conexas
        # Dicionário relacionando cada uma das componentes ao seu respectivo tamanho

    componentes_conexas = [];


    # Instância da busca, para que tenhamos os vértices com as marcações e possamos, intuitivamente, realizar as buscas
    busca_em_grafo = Busca(grafo);
    
    primeira_componente = busca_em_grafo.bfs(busca_em_grafo.vertices[0], retorna_todos=True);
    
    # Atualizamos os dados do objeto do primeiro componente na lista
    componentes_conexas[0].valor = primeira_componente;
    componentes_conexas[0].tamanho = len(primeira_componente);


    # O(n) e dobra o custo de memória
    # Porém, removemos as referências para os vértices "originais" e não precisamos nos preocupar em alterá-los diretamente
    # Além disso, nesse formato, adotamos uma abordagem que leva o maior custo no início do algoritmo, e vai aliviando
    # espaço conforme as componentes forem descobertas
    desmarcados = deepcopy(busca_em_grafo.vertices);  

    while (len(desmarcados) > 0):

        # pega componente
        componente = busca_em_grafo.bfs(desmarcados[0], retorna_todos=True);    
        
        # Componentes serão armazenadas no formato deste objeto
        componentes_conexas.append({ "valor":componente, "tamanho":len(componente)});
        
        # remove os vertices da cópia que forem marcados
        for vertice in desmarcados:
            if(vertice in componente):
                del vertice;
    
    #


    


     

     
    
    # criar uma lista para armazenar as componentes conexas;
    # vai precisar do acesso às marcações que foram feitas anteriormente, então a instância da busca deve ser a mesma.
    # saberemos que terminou caso todos os nós tenham sido marcados (e se não tiver conectividade?; tomar cuidado com esse caso);

    
    pass

n, arestas = ler_arquivo("graph_env/src/test.txt")


""" Testes para matriz de adjacência """

grafo_em_matriz = MatrizAdj(n);
grafo_em_matriz.inserir_arestas(arestas);
print(f"Max: {grau_maximo(grafo_em_matriz)}\n");
print(f"Min: {grau_minimo(grafo_em_matriz)}\n");
print(f"Médio: {grau_medio(grafo_em_matriz)}\n");
print(f"Mediana: {grau_mediana(grafo_em_matriz)}\n");
print(f"Distância entre 3 e 1: {distancia(grafo_em_matriz,Vertice(3),Vertice(1))}")
print(f"Diâmetro: {diametro(grafo_em_matriz)}");

""" Testes para vetor de adjacências """

""" grafo_em_vetor = VetorAdj(n, arestas);
#print(str(vetor_adj_busca.vertices)[1:-1].replace(', ','')); #print chatinho pra kct
print(f"\nMax: {grau_maximo(grafo_em_vetor)}\n");
print(f"Min: {grau_minimo(grafo_em_vetor)}\n");
print(f"Médio: {grau_medio(grafo_em_vetor)}\n");
print(f"Mediana: {grau_mediana(grafo_em_vetor)}\n");
print(f"Distância entre 3 e 1: {distancia(grafo_em_vetor,Vertice(3),Vertice(1))}\n")
print(f"Diâmetro: {diametro(grafo_em_vetor)}") """
