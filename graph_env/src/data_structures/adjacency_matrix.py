from functools import reduce
from math import ceil, floor
from typing import List, Tuple
import numpy as np

class MatrizAdj:

    def __init__(self, num_vertices:int) -> None: 
        # criação dos espaços da matriz
        self.num_vertices:int = num_vertices
        self.matriz:List[List[int]] = np.zeros((num_vertices,num_vertices),dtype=int); #[[0]*self.num_vertices for i in range(self.num_vertices)]
    
    def inserir_arestas(self, arestas:List[Tuple[int]]):
        # modifica o valor da matriz de 0 para 1 quando existir uma aresta (a,b)
        for (a,b) in arestas:
            self.matriz[a-1][b-1] = 1
            self.matriz[b-1][a-1] = 1

    def mostra_matriz(self):
        for i in range(self.num_vertices):
            print(self.matriz[i])#[:i+1]

    def percorrer_vizinhos(self, valor_vertice:int): 
        # Percorremos a linha em busca do números 1;
        vizinhos:List[int] = [];
        for i in range(len(self.matriz)):
            if(self.matriz[valor_vertice-1][i] == 1):
                vizinhos.append(i+1); #precisa de mais um porque i - o índice - começa em 0
        return vizinhos;

    def grau_maximo(self) -> int:
        max:int = 0;
        for i in range(self.num_vertices):
            grau:int = 0;
            for j in range(self.num_vertices):
                grau += self.matriz[i][j];
            if(grau > max):
                max = grau;
        return max;

    def grau_minimo(self) -> int:
        min:int = self.num_vertices-1; #grau máximo é n-1
        for i in range(self.num_vertices):
            grau:int = 0;
            for j in range(self.num_vertices):
                grau += self.matriz[i][j];
            if(grau < min):
                min = grau;
        return min;

    def grau_medio(self) -> np.float32:
        somatorio:int = 0;
        for i in range(self.num_vertices):
            grau:int = 0;
            for j in range(self.num_vertices):
                grau += self.matriz[i][j];
            somatorio += grau;

        return np.float32(somatorio/self.num_vertices);
    
    def grau_mediana(self) -> int:
        
        graus:List[int] = [];

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


# Teste

""" num = 5;
arestas = [(1, 2), (2, 5), (5, 3), (4, 5), (1, 5)];

matriz_teste = MatrizAdj(num)
matriz_teste.inserir_arestas(arestas) """
#matriz_teste.mostra_matriz()
#print(matriz_teste.grau_minimo());
