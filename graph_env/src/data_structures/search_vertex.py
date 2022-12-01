from typing import Union
from numpy import bool8


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


class Vertice_Residual(Vertice):
    def __init__(
        self,
        valor: int,
        pai: int = -1,
        peso: float = 0,
        original_ou_reversa: bool8 = True,
    ) -> None:
        super().__init__(valor, pai, peso)
        self.original_ou_reversa = original_ou_reversa

    def __repr__(self) -> str:

        info_com_peso = super().__repr__()
        original_ou_reversa = (
            "Original" if self.original_ou_reversa == True else "Reversa"
        )
        return f"{info_com_peso} Original/Reversa: {original_ou_reversa}"


# Teste
""" test = Vertice(1);
print(test); """
