'''
Matrizes

É uma estrutura de dados que pode nos ajudar quando temos
muitas variáveis.

Vetor é uma matriz unidimensional.
Matriz é um vetor de vetores (multidimensinal).
Um vetor possui apenas uma linha e várias colunas.

# exemplo de Vetor (Lista)

vetor = [10, 20, 30, 40]

# Exemplo de Matriz == Vetor de Vetores (Lista de Listas)

matriz = [
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
    ]

print(matriz[1][2])

'''

matriz = [
	['joão', 8, 7, 6],
	['pedro', 4.5, 9, 10],
	['marcos', 6, 6, 8],
]

for linha in matriz:
	for col in linha:
		print(str(col) + '\t', end = ' ')
	print('')
