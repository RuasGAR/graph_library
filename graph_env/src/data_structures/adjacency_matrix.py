from functools import reduce
from math import ceil, floor
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
        for i in range(len(self.matriz)):
            if(self.matriz[valor_vertice-1][i] == 1):
                vizinhos.append(i+1); #precisa de mais um porque i - o índice - começa em 0
        return vizinhos;

    def grau_maximo(self):
        max = 0;
        for i in range(self.num_vertices):
            grau = 0;
            for j in range(self.num_vertices):
                grau += self.matriz[i][j];
            if(grau > max):
                max = grau;
        return max;

    def grau_minimo(self):
        min = 0;
        for i in range(self.num_vertices):
            grau = 0;
            for j in range(self.num_vertices):
                grau += self.matriz[i][j];
            if(grau < min):
                min = grau;
        return min;

    def grau_medio(self):
        somatorio = 0;
        for i in range(self.num_vertices):
            grau = 0;
            for j in range(self.num_vertices):
                grau += self.matriz[i][j];
            somatorio += grau;

        return (somatorio/self.num_vertices);
    
    def grau_mediana(self):
        
        graus = [];

        # Calculando os graus
        for i in range(self.num_vertices):
            grau_vertice = int(reduce(lambda x,soma: soma+x, self.matriz[i]));
            graus.append(grau_vertice);

        # Ordenando
        graus.sort()

        # Calculando mediana
        if(self.num_vertices%2 != 0):
            return graus[self.num_vertices//2];
        else:
            return (graus[floor(self.num_vertices/2)] + graus[ceil(self.num_vertices/2)]) / 2 



""" caminho = "../test.txt"
num, aresta = ler_arquivo(caminho)

matriz_teste = MatrizAdj(num)
matriz_teste.inserir_arestas(aresta)
matriz_teste.mostra_matriz() """
