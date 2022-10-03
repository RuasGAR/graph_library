import sys
    # caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1,'/home/ruasgar/Bureau/trabalho_grafos/graph_env/src');

from data_structures.adjacency_vector import VetorAdj
from data_structures.adjacency_matrix import MatrizAdj
from data_structures.search_vertex import Vertice
from searches.busca import Busca
from file_utils.file_handlers import ler_arquivo


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

def componentes_conexas():
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
