from math import floor, ceil
from typing import List, Tuple


class ElementoInicialVetorAdj:
    def __init__(self, valor: int) -> None:
        self.valor: int = valor
        self.vetor_vizinhos: List[int] = []

    def __str__(self) -> str:
        string = f"Nó {self.valor}: -> "
        string += f"Vetor de Vizinhos:{str(self.vetor_vizinhos)}\n"
        string += "================================\n"
        return string


# Teste
""" elemento = ElementoInicialVetorAdj(1);
for i in range(2,6):
    elemento.vetor_vizinhos.append(i)

print(elemento); """

# ==================================================================================================================


class VetorAdj:
    def __init__(
        self,
        num_vertices: int,
        arestas: List[Tuple[int]],
        container: List[ElementoInicialVetorAdj],
    ) -> None:
        self.num_vertices = num_vertices
        self.arestas = arestas
        self.container = container

    @classmethod
    def formato_tradicional(
        cls,
        num_vertices: int,
        arestas: List[Tuple[int]],
        tem_pesos=False,
        direcionado=False,
    ):

        # Percorrer todas as arestas, criando um elemento inicial para cada vértice
        container: List[ElementoInicialVetorAdj.__class__] = [
            ElementoInicialVetorAdj(x) for x in range(1, num_vertices + 1)
        ]

        # Agora, vamos preencher os vizinhos de acordo com as arestas
        # Arestas: [(1, 2), (2, 5), (5, 3), (4, 5), (1, 5)]
        # Primeiro par: (1,2)
        # Vamos à posição 0 do container, que no nosso caso, simboliza a posição 1 do que vemos em aula
        # (par[0] - 1) = 1 ---------- esse valor vem da tupla, mas que na prática é o espaço 0
        # Ao vetor de vizinhos, adicionamos o outro componente do par! Nesse caso, é o valor 2, presente em par[1]
        # Também temos de fazer o contrário: par[1] precisa saber que par[0] é seu vizinho
        # O valor que damos ao método .append é o valor real, e não a posição no container.

        for par in arestas:

            # append de uma tupla com (destino, peso_para_o_destino)
            # grafo pode ser direcionado ou não (parte 3)
            if tem_pesos == True:
                container[par[0] - 1].vetor_vizinhos.append((par[1], par[2]))
                if direcionado != True:
                    container[par[1] - 1].vetor_vizinhos.append((par[0], par[2]))
            else:
                container[par[0] - 1].vetor_vizinhos.append(par[1])
                if direcionado != True:
                    container[par[1] - 1].vetor_vizinhos.append(par[0])

        return cls(num_vertices=num_vertices, arestas=arestas, container=container)

    @classmethod
    def formato_com_fluxo(
        cls,
        num_vertices: int,
        arestas: List[Tuple[int]],
    ):
        # Aqui, assumimos que o grafo é direcionado e com pesos por padrão
        # As aretas terão formato de 4-upla: (vertice1, vertice2, capacidade, fluxo_passante)

        container: List[ElementoInicialVetorAdj.__class__] = [
            ElementoInicialVetorAdj(x) for x in range(1, num_vertices + 1)
        ]

        for a in arestas:
            container[a[0] - 1].vetor_vizinhos.append((a[1], a[2], a[3]))

        return cls(num_vertices=num_vertices, arestas=arestas, container=container)

    # Na verdade, uma coisa mudará: agora, a lista de vetores vizinhos pode ser uma tupla de 2 elementos
    # ou mais. No primeiro caso, temos o padrão de grafos sem pesos. Quando existem mais parâmetros,
    # pode haver peso, capacidade e fluxo passante.

    def percorrer_vizinhos(self, valor_vertice: int) -> List[int]:

        # Se forem arestas somente com vértices (sem pesos)
        if len(self.arestas[0]) == 2:
            return self.container[valor_vertice - 1].vetor_vizinhos

        return list(
            map(
                lambda nupla: nupla[0], self.container[valor_vertice - 1].vetor_vizinhos
            )
        )

    def imprimir(self) -> None:
        for elemento in self.container:
            print(elemento)

    def grau_maximo(self) -> int:
        max: int = len(self.container[0].vetor_vizinhos)
        for i in range(1, len(self.container)):
            grau: int = len(self.container[i].vetor_vizinhos)
            if grau > max:
                max = grau
        return max

    def grau_minimo(self) -> int:
        min: int = len(self.container[0].vetor_vizinhos)
        for i in range(1, len(self.container)):
            grau: int = len(self.container[i].vetor_vizinhos)
            if grau < min:
                min = grau
        return min

    def grau_medio(self) -> float:
        somatorio: int = 0
        for i in range(len(self.container)):
            somatorio += len(self.container[i].vetor_vizinhos)
        return somatorio / self.num_vertices

    def grau_mediana(self) -> int:
        # Primeiro, precisamos pegar todos os graus. Podemos fazer isso com uma abordagem funcional
        graus: List[int] = list(
            map(lambda vertice: len(vertice.vetor_vizinhos), self.container)
        )
        # Ordenando a lista
        graus.sort()
        # Retorna None;
        # Calculando a mediana:
        if self.num_vertices % 2 != 0:
            return graus[self.num_vertices // 2]
        else:
            return (
                graus[floor(self.num_vertices / 2)] + graus[ceil(self.num_vertices / 2)]
            ) / 2


# ==========================================================================================================================

# Testes

########## Primeira Parte (BFS, DFS, e etc)

""" teste_vetor_adj = VetorAdj.formato_tradicional(5,[(1, 2), (2, 5), (5, 3), (4, 5), (1, 5)])
#teste_vetor_adj.imprimir()"""
# print("Vizinhos de 2: " + str(teste_vetor_adj.percorrer_vizinhos(2)));
# print("Vizinhos de 5: " + str(teste_vetor_adj.percorrer_vizinhos(5))); """

########## Segunda Parte (Dijkstra)

""" teste_vetor_adj = VetorAdj.formato_tradicional(
    5,
    [(1, 2, 0.1), (2, 5, 0.2), (5, 3, 5), (3, 4, -9.5), (4, 5, 2.3), (1, 5, 1)],
    tem_pesos=True,
)
# teste_vetor_adj.imprimir()
print("Vizinhos de 2: " + str(teste_vetor_adj.percorrer_vizinhos(2)))
print("Vizinhos de 5: " + str(teste_vetor_adj.percorrer_vizinhos(5))) """

########## Teceira Parte (Fluxo -> necessidade de overload)

# Adaptação dos anteriores
""" teste_vetor_adj = VetorAdj.formato_tradicional(
    5, [(1, 2), (2, 5), (5, 3), (4, 5), (1, 5)]
)
teste_vetor_adj.imprimir() """

# Implementação da variação com fluxo e capacidade
# Exemplo do slide 7 da aula 16, com s=3 e t=4
""" teste_vetor_adj = VetorAdj.formato_com_fluxo(
    4, [(3, 1, 20, 10), (1, 4, 10, 5), (1, 2, 30, 5), (3, 2, 10, 5), (2, 4, 20, 10)]
)
teste_vetor_adj.imprimir() """
