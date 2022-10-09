#import sys
    # caution: path[0] is reserved for script path (or '' in REPL)
#sys.path.insert(1,'/home/ruasgar/Bureau/trabalho_grafos/graph_env/src');

from numpy import random
from data_structures.adjacency_vector import VetorAdj
from data_structures.search_vertex import Vertice
from data_structures.adjacency_matrix import MatrizAdj
from searches.busca import Busca
from file_utils.file_handlers import ler_arquivo
from time import time 

def __main__():

    tempos_medios_matriz = questao_2(4, "matriz");
    tempos_medios_vetor = questao_2(4, "vetor");

    print(f"Tempo médio de Busca em Largura (MatrizAdj) no Grafo 4: ",tempos_medios_matriz[0]);
    print(f"Tempo médio de Busca em Profundidade (MatrizAdj) no Grafo 4: ",tempos_medios_matriz[1]);

    print(f"Tempo médio de Busca em Largura (VetorAdj) no Grafo 4: ",tempos_medios_vetor[0]);
    print(f"Tempo médio de Busca em Profundidade (VetorAdj) no Grafo 4: ",tempos_medios_vetor[1]);

    

# Estudos de Caso

# Ponto 2:

# Grafo 2
def questao_2(grafo_num:int, graph_repr:str):

    # Lê os arquivos
    n, arestas = ler_arquivo(f"grafo_{grafo_num}.txt")

    # Inicializa os arrays de tempo e vertices a servirem de input; e os sorteia;
    todos_tempos_bfs = [];
    todos_tempos_deep = [];
    vertices_iniciais = [];
    for i in range(1000):
        vertices_iniciais.append(random.randint(0,968))

    # Cria o grafo na representação pedida
    if(graph_repr == "matriz"):
        grafo = MatrizAdj(n);
        grafo.inserir_arestas(arestas);
    elif(graph_repr == "vetor"):
        grafo = VetorAdj(n, arestas);

    # Instanciando busca para o grafo
    busca_em_grafo = Busca(grafo)

    for num in range(100): 

        print(num);

        # BUSCA EM LARGURA
        tempo_inicial_bfs = time()
        busca_em_grafo.bfs(Vertice(vertices_iniciais[num]));
        tempo_final_bfs = time();
    
        intervalo_bfs = tempo_final_bfs - tempo_inicial_bfs;
        todos_tempos_bfs.append(intervalo_bfs);
        
        # BUSCA EM PROFUNDIDADE
        tempo_inicial_deep = time();
        busca_em_grafo.dfs(Vertice(vertices_iniciais[num]));
        tempo_final_deep = time();

        intervalo_deep = tempo_final_deep - tempo_inicial_deep;
        todos_tempos_deep.append(intervalo_deep);

    tempo_medio_bfs = sum(todos_tempos_bfs)/len(vertices_iniciais);
    tempo_medio_deep = sum(todos_tempos_deep)/len(vertices_iniciais);

    return [tempo_medio_bfs, tempo_medio_deep];

    

__main__();