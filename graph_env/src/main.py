from data_structures.adjacency_vector import VetorAdj
from file_utils.file_handlers import ler_arquivo
from os import getcwd, path



def __main__():

    caminho = "test.txt"

    numero_vertices, arestas = ler_arquivo(path.join(getcwd(),caminho));

    vetor_de_adjacencia = VetorAdj(numero_vertices, arestas);

    for item in vetor_de_adjacencia.container:
        print(f"Valor:{item.valor+1}");
        print(f"Vetor Vizinhos:{list(map(lambda x: x+1,item.vetor_vizinhos))}");
        print("================================================================");

__main__();
