import sys
    # caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1,'/home/ruasgar/Bureau/trabalho_grafos/graph_env/src');

from file_utils.file_handlers import ler_arquivo
from data_structures.adjacency_vector import VetorAdj
from data_structures.adjacency_matrix import MatrizAdj
from data_structures.search_vertex import Vertice
from collections import deque

class Busca:

    def __init__(self,grafo) -> None:
        self.grafo = grafo;
        self.vertices = [];
        if(isinstance(grafo, VetorAdj)):
            self.vertices = [Vertice(x.valor) for x in grafo.container] # Quantidade de elementos no vetor container é n 
        elif(isinstance(grafo,MatrizAdj)):
            self.vertices = [Vertice(x) for x in range(len(grafo.matriz))] #Quantidade de linhas da matriz é n

    def bfs(self, vertice_s):
        # Desmarcar todos os vértices
        # Por natureza, já são desmarcados, mas alterando por referência, é sempre bom rever
        for no in self.vertices:
            no.marcador = False;
            no.pai = None;
            no.nivel = 0;

        # Setar fila Q
        fila = deque();

        # Marcar s, denotar seu nível, e inserir na fila
        self.vertices[vertice_s.valor-1].marcador = True;
        #vertice_s.nivel = 0; desnecessário, mas vou deixar o comentário pra lembrar
        fila.append(vertice_s);

        # Loop
        while (len(fila) != 0):      
            #print(fila);  
            v = fila.popleft();
            for w in (grafo.percorrer_vizinhos(v.valor)):
                if (self.vertices[w-1].marcador == False):
                    self.vertices[w-1].marcador = True;
                    self.vertices[w-1].nivel = v.nivel + 1;
                    self.vertices[w-1].pai = v.valor; #o ideal seria o endereço de v, mas...
                    fila.append(self.vertices[w-1])

        return list(filter(lambda x: x.marcador == True, self.vertices));

n, arestas = ler_arquivo("graph_env/src/test.txt")

grafo = VetorAdj(n,arestas)

buscador = Busca(grafo);
#print(str(buscador.vertices)[1:-1].replace(', ','')); #print chatinho pra kct
print(buscador.bfs(Vertice(3))) 
#buscador.bfs(Vertice(2))
    
        
