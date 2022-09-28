from initial_element import ElementoInicialVetorAdj

class VetorAdj:
    
    def __init__(self,num_vertices,arestas):

        #Percorrer todas as arestas, criando um elemento inicial para cada vértice
        self.container = [ElementoInicialVetorAdj(x) for x in range(num_vertices)]

        # Agora, vamos preencher os vizinhos de acordo com as arestas
        # Arestas: [(1, 2), (2, 5), (5, 3), (4, 5), (1, 5)]
            # Primeiro par: (1,2)
                # Vamos à posição 0 do container, que no nosso caso, simboliza a posição 1 do que vemos em aula
                # (par[0] - 1) = 1 ---------- esse valor vem da tupla, mas que na prática é o espaço 0
                # Ao vetor de vizinhos, adicionamos o outro componente do par! Nesse caso, é o valor 2, presente em par[1]
                # Também temos de fazer o contrário: par[1] precisa saber que par[0] é seu vizinho

        for par in arestas:
            self.container[par[0]-1].vetor_vizinhos.append(par[1]-1)
            self.container[par[1]-1].vetor_vizinhos.append(par[0]-1) 

    def percorrer_vizinhos(self,valor_vertice:int):
        return self.container[valor_vertice].vetor_vizinhos;
        
    def __repr__(self) -> str:
        for v in self.container:
            print(v);