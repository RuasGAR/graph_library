from typing import Union


class Vertice:
    def __init__(
        self,
        valor: int,
        pai: int = -1,
        peso: float = 0.0,
    ) -> None:
        self.valor: int = valor
        self.marcador: bool = False
        self.pai: Union[int, None] = pai if pai else None
        self.nivel: int = 0
        self.peso = peso

    def __repr__(self) -> str:

        if self.pai == None or self.pai == -1:
            repr_pai = "Raiz"
        else:
            repr_pai = self.pai

        # Segunda Parte
        return f"Nó {self.valor}: ------> Pai: {repr_pai}; Peso: " + "{0:.2f}".format(
            self.peso
        )

        # Primeira Parte:
        # return f"Nó {self.valor}: ----> Pai: {self.pai}; Nivel: {self.nivel}\n"


# Teste
""" test = Vertice(1);
print(test); """
