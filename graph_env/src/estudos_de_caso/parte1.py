from typing import List, Union
from numpy import random
from data_structures.adjacency_vector import VetorAdj
from data_structures.search_vertex import Vertice
from data_structures.adjacency_matrix import MatrizAdj
from searches.busca import Busca
from file_utils.file_handlers import ler_arquivo
from extra_functions import functions
from time import time
import os

# Função auxiliar, que pode ser adaptada para pedido de entrada
def repr_e_leitura(
    grafo_num: int, grafo_repr: str
) -> List[Union[List[Union[MatrizAdj, VetorAdj]], int]]:

    n, arestas = ler_arquivo(f"grafo_{grafo_num}.txt")

    if grafo_repr == "matriz":
        grafo = MatrizAdj(n)
        grafo.inserir_arestas(arestas)
    elif grafo_repr == "vetor":
        grafo = VetorAdj.formato_tradicional(n, arestas)

    return [grafo, n, len(arestas)]


# QUESTÕES 2 E 3
def tempos_medios(grafo_num: int, graph_repr: str):

    # Lê os arquivos
    n, arestas = ler_arquivo(f"grafo_{grafo_num}.txt")

    # Inicializa os arrays de tempo e vertices a servirem de input; e os sorteia;
    todos_tempos_bfs = []
    todos_tempos_deep = []
    vertices_iniciais = []
    for i in range(1000):
        vertices_iniciais.append(random.randint(0, n))

    # Cria o grafo na representação pedida
    if graph_repr == "matriz":
        grafo = MatrizAdj(n)
        grafo.inserir_arestas(arestas)
    elif graph_repr == "vetor":
        grafo = VetorAdj.formato_tradicional(n, arestas)

    # Instanciando busca para o grafo
    busca_em_grafo = Busca(grafo)

    for num in range(1000):

        # print(num) - apenas para monitoramento

        # BUSCA EM LARGURA
        tempo_inicial_bfs = time()
        busca_em_grafo.bfs(Vertice(vertices_iniciais[num]))
        tempo_final_bfs = time()

        intervalo_bfs = tempo_final_bfs - tempo_inicial_bfs
        todos_tempos_bfs.append(intervalo_bfs)

        # BUSCA EM PROFUNDIDADE
        tempo_inicial_deep = time()
        busca_em_grafo.dfs(Vertice(vertices_iniciais[num]))
        tempo_final_deep = time()

        intervalo_deep = tempo_final_deep - tempo_inicial_deep
        todos_tempos_deep.append(intervalo_deep)

    tempo_medio_bfs = sum(todos_tempos_bfs) / len(vertices_iniciais)
    tempo_medio_deep = sum(todos_tempos_deep) / len(vertices_iniciais)

    return [tempo_medio_bfs, tempo_medio_deep]


# QUESTÃO 4
def descobrir_pais(grafo_num: int):

    print("Vou começar a descobrir os pais no grafo", grafo_num)

    grafo, n, arestas = repr_e_leitura(grafo_num, "vetor")

    pais_a_determinar = [10, 20, 30]
    vertices_iniciais = [1, 2, 3]

    busca_em_grafo = Busca(grafo)

    for vertice in vertices_iniciais:

        # BFS
        print("Rodando BFS no vertice: ", vertice)
        largura = busca_em_grafo.bfs(Vertice(vertice))
        for v in largura:
            if v.valor in pais_a_determinar:
                print(f"Temos que {v.valor} tem a seguinte estrutura")
                print(v)

        # DFS

        print("Rodando DFS no vertice: ", vertice)
        profundidade = busca_em_grafo.dfs(Vertice(vertice))
        for u in profundidade:
            if u.valor in pais_a_determinar:
                print(f"Temos que {u.valor} tem a seguinte estrutura")
                print(u)


# QUESTÃO 5
def questao_distancias(grafo_num: int, grafo_repr: str):

    print(
        "Estou analisando as distâncias do grafo ",
        grafo_num,
        "com a representação de ",
        grafo_repr,
    )

    pares = [(10, 20), (10, 30), (20, 30)]

    grafo = repr_e_leitura(grafo_num, grafo_repr)

    for i in range(0, 3):
        resposta = functions.distancia(grafo, pares[i][0], pares[i][1])
        print(
            f"A distância entre {pares[i][0]} e {pares[i][1]} no grafo {grafo_num} é de {resposta}!\n"
        )


# QUESTÃO 6
def print_informacao_grafo(formato: str) -> None:

    for i in range(2, 7):

        grafo, num_vertices, num_arestas = repr_e_leitura(i, formato)
        comp_conexas = functions.componentes_conexas(grafo)

        with open(os.path.join(os.getcwd(), f"grafo_{i}_output.txt"), "w") as file:
            file.write(f"Analisando grafo {i} na representação em {formato}.")
            file.write(f"Número de Vértices: {num_vertices}\n")
            file.write(f"Número de Arestas: {num_arestas}\n")
            file.write(f"Grau Máximo: {functions.grau_maximo(grafo)}\n")
            file.write(f"Grau Mínimo: {functions.grau_minimo(grafo)}\n")
            file.write(f"Grau Médio: {functions.grau_medio(grafo)}\n")
            file.write(f"Mediana do Grau: {functions.grau_mediana(grafo)}\n")
            file.write(f"Quantidade de componentes conexas: {len(comp_conexas)}\n")
            file.write(
                "Componentes conexas, impressas da maior (com mais vértices) para a menor: \n"
            )
            for componente in comp_conexas:
                file.write(
                    "Componente de tamanho {0}: \n".format(str(componente["tamanho"]))
                )
                for vertice in componente["valor"]:
                    file.write("{0}\n".format(str(vertice.valor)))
                file.write(f"Fim da componente.\n\n")

            file.write("Término de análise do grafo.\n")
            file.close()


"""
    TESTES DE IMPRESSÃO PARA OS TEMPOS MÉDIOS

    tempos_medios_matriz = questao_2(4, "matriz")
    tempos_medios_vetor = questao_2(4, "vetor")

    print(
        f"Tempo médio de Busca em Largura (MatrizAdj) no Grafo 4: ",
        tempos_medios_matriz[0],
    )
    print(
        f"Tempo médio de Busca em Profundidade (MatrizAdj) no Grafo 4: ",
        tempos_medios_matriz[1],
    )

    print(
        f"Tempo médio de Busca em Largura (VetorAdj) no Grafo 4: ",
        tempos_medios_vetor[0],
    )
    print(
        f"Tempo médio de Busca em Profundidade (VetorAdj) no Grafo 4: ",
        tempos_medios_vetor[1],
    ) 
"""
