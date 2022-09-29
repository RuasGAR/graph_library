from file_utils.file_handlers import ler_arquivo


class MatrizAdj:

    def __init__(self, num_vertices) -> None: 
        # criação dos espaços da matriz
        self.num_vertices = num_vertices
        self.matriz = [[0]*self.num_vertices for i in range(self.num_vertices)]
    
    def inserir_arestas(self, arestas):
        # modifica o valor da matriz de 0 para 1 quando existir uma aresta (a,b)
        for (a,b) in arestas:
            self.matriz[a-1][b-1] = 1
            self.matriz[b-1][a-1] = 1

    def mostra_matriz(self):
        for i in range(self.num_vertices):
            print(self.matriz[i])#[:i+1]

    def percorrer_vizinhos(self, valor_vertice):
        # por estarmos com uma matriz triangular inferior, vamos pegar a linha daquele vértice 
        # nessa linha, precisamos percorrer e gravar o índice de todos os vértices que tiverem valor igual a 1
        vizinhos = [];
        for i in range(self.matriz[valor_vertice]):
            if(self.matriz[valor_vertice][i] == 1):
                vizinhos.append(i);
        return vizinhos;

""" caminho = "test.txt"
num, aresta = ler_arquivo(caminho)

matriz_teste = MatrizAdj(num)
matriz_teste.inserir_arestas(aresta)
matriz_teste.mostra_matriz() """
