"""Lê um texto e um número inteiro e repete o texto N vezes.

Uso:
	python resolucoes/repet_txt.py

O script pede um texto e a quantidade de repetições e exibe o resultado.
"""

from typing import Tuple


def ler_texto_e_repeticoes() -> Tuple[str, int]:
	texto = input("Digite o texto a ser repetido: ")
	while True:
		try:
			n = int(input("Digite o número de repetições (inteiro >= 0): "))
			if n < 0:
				print("Use um inteiro não-negativo.")
				continue
			return texto, n
		except ValueError:
			print("Entrada inválida. Informe um número inteiro.")


def repetir(texto: str, n: int) -> str:
	if n <= 0:
		return ""
	return " ".join([texto] * n)


def main() -> None:
	texto, n = ler_texto_e_repeticoes()
	resultado = repetir(texto, n)
	print("Resultado:", resultado)


if __name__ == "__main__":
	main()