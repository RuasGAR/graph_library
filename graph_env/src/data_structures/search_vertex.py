class Vertice:

    # Temos um parâmetro que vai ocupar memória desnecessária, mas ganhamos na simplificação das chamadas 
    # e na reutilização

    def __init__(self, valor) -> None:
        self.valor = valor;
        self.marcador = False;
        self.pai = None;
        self.nivel = 0;
    
    def __repr__(self) -> str:
        
        if self.pai == None:
            self.pai = "Raiz"

        return f"Nó {self.valor}: ----> Pai: {self.pai}; Nivel: {self.nivel}\n";  



"""     def reset(self):
        self.marcador = False;
        self.pai = None;
        self.nivel = 0; """

    