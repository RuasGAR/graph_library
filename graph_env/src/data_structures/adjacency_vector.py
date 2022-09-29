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
        if(valor_vertice > 0):
            return self.container[valor_vertice-1].vetor_vizinhos;
    
    def imprimir(self):
        for elemento in self.container:
            print(elemento)

# ==========================================================================================================================
# Testes

""" teste_vetor_adj = VetorAdj(5,[(1, 2), (2, 5), (5, 3), (4, 5), (1, 5)])
#teste_vetor_adj.imprimir()
print("Vizinhos de 2: " + str(teste_vetor_adj.percorrer_vizinhos(2)));
print("Vizinhos de 5: " + str(teste_vetor_adj.percorrer_vizinhos(5))); """

