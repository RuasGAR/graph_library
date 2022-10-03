from math import floor, ceil

class ElementoInicialVetorAdj:
    
    def __init__(self, valor) -> None:
        self.valor = valor
        self.vetor_vizinhos = []

    def __str__(self) -> str:
        string = f"Nó {self.valor}: -> " 
        string += f"Vetor de Vizinhos:{str(self.vetor_vizinhos)}\n"
        string += "================================\n";
        return string

# Teste
""" elemento = ElementoInicialVetorAdj(1);
for i in range(2,6):
    elemento.vetor_vizinhos.append(i)

print(elemento); """

#==================================================================================================================

class VetorAdj:
    
    def __init__(self,num_vertices,arestas):

        #Percorrer todas as arestas, criando um elemento inicial para cada vértice
        self.container = [ElementoInicialVetorAdj(x) for x in range(1,num_vertices+1)]
        self.num_vertices = num_vertices;

        # Agora, vamos preencher os vizinhos de acordo com as arestas
        # Arestas: [(1, 2), (2, 5), (5, 3), (4, 5), (1, 5)]
            # Primeiro par: (1,2)
                # Vamos à posição 0 do container, que no nosso caso, simboliza a posição 1 do que vemos em aula
                # (par[0] - 1) = 1 ---------- esse valor vem da tupla, mas que na prática é o espaço 0
                # Ao vetor de vizinhos, adicionamos o outro componente do par! Nesse caso, é o valor 2, presente em par[1]
                # Também temos de fazer o contrário: par[1] precisa saber que par[0] é seu vizinho
                # O valor que damos ao método .append é o valor real, e não a posição no container. 

        for par in arestas:
            self.container[par[0]-1].vetor_vizinhos.append(par[1])
            self.container[par[1]-1].vetor_vizinhos.append(par[0]) 
        #print(self.container)

    def percorrer_vizinhos(self,valor_vertice:int):
        return self.container[valor_vertice-1].vetor_vizinhos;
    
    def imprimir(self):
        for elemento in self.container:
            print(elemento)

    def grau_maximo(self):
        max = len(self.container[0].vetor_vizinhos);
        for i in range(1,len(self.container)):
            grau = len(self.container[i].vetor_vizinhos); 
            if(grau > max):
                max = grau;
        return max;
                
    def grau_minimo(self):
        min = len(self.container[0].vetor_vizinhos);
        for i in range(1,len(self.container)):
            grau = len(self.container[i].vetor_vizinhos); 
            if(grau < min):
                min = grau;
        return min;

    def grau_medio(self):
        somatorio = 0;
        for i in range(len(self.container)):
            somatorio += len(self.container[i].vetor_vizinhos);
        return (somatorio / self.num_vertices);
    
    def grau_mediana(self):
        # Primeiro, precisamos pegar todos os graus. Podemos fazer isso com uma abordagem funcional
        graus = list(map(lambda vertice:len(vertice.vetor_vizinhos),self.container));
        # Ordenando a lista
        graus.sort(); # Retorna None;
        # Calculando a mediana:
        if(self.num_vertices%2 != 0):
            return graus[self.num_vertices//2];
        else:
            return (graus[floor(self.num_vertices/2)] + graus[ceil(self.num_vertices/2)]) / 2 




# ==========================================================================================================================
# Testes

""" teste_vetor_adj = VetorAdj(5,[(1, 2), (2, 5), (5, 3), (4, 5), (1, 5)])
#teste_vetor_adj.imprimir()
print("Vizinhos de 2: " + str(teste_vetor_adj.percorrer_vizinhos(2)));
print("Vizinhos de 5: " + str(teste_vetor_adj.percorrer_vizinhos(5))); """

