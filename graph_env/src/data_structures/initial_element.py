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