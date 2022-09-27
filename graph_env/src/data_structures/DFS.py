from file_utils.file_handlers import ler_arquivo

class DFS:
    def __init__(self,numero_vertices,matriz) -> None:
        self.vertices = numero_vertices
        self.matriz = [[0]*self.num_vertices for i in range(self.num_vertices)]

    def dfs(self,inicio,visitado):
        print(inicio)
        visitado[inicio] = True
        for i in range(self.vertices):
            if (self.matriz[inicio][i] == 1 and (not visitado[i])):
                self.dfs(i,visitado)