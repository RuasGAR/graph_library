from typing import Union


class Vertice:

    # Temos um parâmetro que vai ocupar memória desnecessária, mas ganhamos na simplificação das chamadas
    # e na reutilização

    def __init__(
        self,
        valor: int,
        pai: int,
        peso: float = 0.0,
    ) -> None:
        self.valor: int = valor
        self.marcador: bool = False
        self.pai: Union[int, None] = pai if pai else None
        self.nivel: int = 0
        self.peso = peso

    def __repr__(self) -> str:

        if self.pai == None or self.pai == -1:
            self.pai = "Sou Raiz"

        # Segunda Parte
        return f"Nó {self.valor}: ------> Pai: {self.pai}; Peso: " + "{0:.2f}".format(
            self.peso
        )

        # Primeira Parte:
        # return f"Nó {self.valor}: ----> Pai: {self.pai}; Nivel: {self.nivel}\n"


# Teste
""" test = Vertice(1);
print(test); """
