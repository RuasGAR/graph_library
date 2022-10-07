from typing import Union

class Vertice:

    # Temos um parâmetro que vai ocupar memória desnecessária, mas ganhamos na simplificação das chamadas 
    # e na reutilização

    def __init__(self, valor:int) -> None:
        self.valor:int = valor;
        self.marcador:bool = False;
        self.pai:Union[int,None] = None;
        self.nivel:int = 0;
    
    def __repr__(self) -> str:
        
        if self.pai == None:
            self.pai = "Raiz"

        return f"Nó {self.valor}: ----> Pai: {self.pai}; Nivel: {self.nivel}\n";  

# Teste
""" test = Vertice(1);
print(test); """
