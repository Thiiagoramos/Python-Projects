"""Recebe dois dados do usuário e concatena-os em uma única string.

Uso:
	python resolucoes/concat_dados.py

O script pede dois valores ao usuário e imprime a concatenação.
"""

from typing import Tuple


def ler_dois_dados() -> Tuple[str, str]:
	primeiro = input("Digite o primeiro dado: ")
	segundo = input("Digite o segundo dado: ")
	return primeiro, segundo


def concatena(a: str, b: str) -> str:
	return f"{a}{b}"


def main() -> None:
	a, b = ler_dois_dados()
	resultado = concatena(a, b)
	print("Resultado:", resultado)


if __name__ == "__main__":
	main()