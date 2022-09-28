import sys
    # caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1,'/home/ruasgar/Bureau/trabalho_grafos/graph_env/src');

from file_utils.file_handlers import ler_arquivo
from data_structures.adjacency_vector import VetorAdj
from data_structures.adjacency_matrix import MatrizAdj
from data_structures.search_vertex import Vertice
from collections import deque

class Busca:

    def __init__(self,vertices) -> None:
        
        # QUAL É O MELHOR JEITO DE GUARDAR?

        pass

        # ESTÁ FALTANDO ABSTRAIR A ESTRUTURA DE DADOS
    def bfs(self, vertice_s):
        # Desmarcar todos os vértices
        # Por natureza, já são desmarcados, mas alterando por referência, é sempre bom rever
        for no in self.vertices.container:
            no.reset();
        
        #ATÉ AQUI TÁ CERTO

        # Setar fila Q
        fila = deque();

        # Marcar s, denotar seu nível, e inserir na fila
        self.vertices.container[vertice_s.valor-1].marcador = True;
        vertice_s.nivel = 0;
        fila.append(vertice_s);

        # Loop
        while (len(fila) != 0):      
            #print(fila);  
            v = fila.popleft();
            for w in (self.vertices.percorrer_vizinhos(v.valor)):
                if (w.marcador == False):
                    w.marcador = True;
                    w.nivel = v.nivel + 1;
                    w.pai = v.valor; #o ideal seria o endereço de v, mas...
                    fila.append(w)

        return list(filter(lambda x: x.marcador == True, self.vertices.container));

n, arestas = ler_arquivo("graph_env/src/test.txt")

grafo = VetorAdj(n,arestas)

#print(grafo);

buscador = Busca(grafo);
print(buscador.bfs(Vertice(2)))
#buscador.bfs(Vertice(2))
    
        
