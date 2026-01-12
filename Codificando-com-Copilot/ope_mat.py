"""Lê dois números do usuário e executa uma operação simples entre eles.

Uso:
	python resolucoes/ope_mat.py

O script pede dois números e a operação (+, -, *, /) e imprime o resultado.
"""

from typing import Tuple


def ler_dois_numeros() -> Tuple[float, float]:
	while True:
		try:
			a = float(input("Digite o primeiro número: "))
			break
		except ValueError:
			print("Entrada inválida. Use um número (ex: 3.14).")
	while True:
		try:
			b = float(input("Digite o segundo número: "))
			break
		except ValueError:
			print("Entrada inválida. Use um número (ex: 2).")
	return a, b


def escolher_operacao() -> str:
	ops = "+-*/"
	while True:
		op = input("Escolha a operação (+, -, *, /): ").strip()
		if op in ops:
			return op
		print("Operação inválida. Escolha entre +, -, *, /." )


def calcular(a: float, b: float, op: str):
	if op == "+":
		return a + b
	if op == "-":
		return a - b
	if op == "*":
		return a * b
	if op == "/":
		if b == 0:
			return "Erro: divisão por zero"
		return a / b


def main() -> None:
	a, b = ler_dois_numeros()
	op = escolher_operacao()
	resultado = calcular(a, b, op)
	print("Resultado:", resultado)


if __name__ == "__main__":
	main()