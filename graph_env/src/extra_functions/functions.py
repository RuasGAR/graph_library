import sys
    # caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1,'/home/ruasgar/Bureau/trabalho_grafos/graph_env/src');

from data_structures.adjacency_vector import VetorAdj
from data_structures.adjacency_matrix import MatrizAdj
from file_utils.file_handlers import ler_arquivo


def grau_maximo(grafo):
    return grafo.grau_maximo();

def grau_minimo(grafo):
    return grafo.grau_minimo();

def grau_medio(grafo):
    return grafo.grau_medio();

def grau_mediana(grafo):
    return grafo.grau_mediana();

n, arestas = ler_arquivo("graph_env/src/test.txt")


""" Testes para matriz de adjacência """

grafo_em_matriz = MatrizAdj(n);
grafo_em_matriz.inserir_arestas(arestas);
print(f"Max: {grau_maximo(grafo_em_matriz)}\n");
print(f"Min: {grau_minimo(grafo_em_matriz)}\n");
print(f"Médio: {grau_medio(grafo_em_matriz)}\n");
print(f"Mediana: {grau_mediana(grafo_em_matriz)}\n");

""" Testes para vetor de adjacências """

grafo_em_vetor = VetorAdj(n, arestas);
#print(str(vetor_adj_busca.vertices)[1:-1].replace(', ','')); #print chatinho pra kct

