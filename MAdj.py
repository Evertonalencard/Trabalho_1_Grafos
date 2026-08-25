import matplotlib.pyplot as plt

class MAdj:
	"""Matriz de adjacência booleana entre os 26 estados brasileiros + Distrito Federal.

	Ordem usada (índices correspondem às linhas/colunas da matriz):
	['AC','AL','AM','AP','BA','CE','DF','ES','GO','MA','MG','MS','MT',
	 'PA','PB','PE','PI','PR','RJ','RN','RO','RR','RS','SC','SP','SE','TO']

	`True` indica fronteira entre os estados correspondentes.
	"""

	STATES = [
		'AC','AL','AM','AP','BA','CE','DF','ES','GO','MA','MG','MS','MT',
		'PA','PB','PE','PI','PR','RJ','RN','RO','RR','RS','SC','SP','SE','TO'
	]

	MATRIX = [
		# AC
		[False, False, True,  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True,  False, False, False, False, False, False],
		# AL
		[False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, True,  False, False, False, False, False, False, False, False, False, True,  False],
		# AM
		[True,  False, False, False, False, False, False, False, False, False, False, False, True,  True,  False, False, False, False, False, False, True,  True,  False, False, False, False, False],
		# AP
		[False, False, False, False, False, False, False, False, False, False, False, False, False, True,  False, False, False, False, False, False, False, False, False, False, False, False, False],
		# BA
		[False, True,  False, False, False, False, False, True, True,  False, True,  False, False, False, False, True,  True,  False, False, False, False, False, False, False, False, True,  True ],
		# CE
		[False, False, False, False, False, False, False, False, False, False, False, False, False, False, True,  True,  True,  False, False, True,  False, False, False, False, False, False, False],
		# DF
		[False, False, False, False, False, False, False, False, True,  False, False,  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
		# ES
		[False, False, False, False, True, False, False, False, False, False, True,  False, False, False, False, False, False, False, True,  False, False, False, False, False, False, False, False],
		# GO
		[False, False, False, False, True,  False, True,  False, False, False, True,  True,  True,  False, False, False, False, False, False, False, False, False, False, False, False, False, True ],
		# MA
		[False, False, False, False, False, False, False, False, False, False, False, False, False, True,  False, False, True,  False, False, False, False, False, False, False, False, False, True ],
		# MG
		[False, False, False, False, True,  False, False,  True,  True,  False, False, True,  False, False, False, False, False, False, True,  False, False, False, False, False, True,  False, False],
		# MS
		[False, False, False, False, False, False, False, False, True,  False, True,  False, True,  False, False, False, False, True,  False, False, False, False, False, False, True,  False, False],
		# MT
		[False, False, True,  False, False, False, False, False, True,  False, False, True,  False, True,  False, False, False, False, False, False, True,  False, False, False, False, False, True ],
		# PA
		[False, False, True,  True,  False, False, False, False, False, True,  False, False, True,  False, False, False, False, False, False, False, False, True, False, False, False, False, True ],
		# PB
		[False, False, False, False, False, True,  False, False, False, False, False, False, False, False, False, True,  False, False, False, True,  False, False, False, False, False, False, False],
		# PE
		[False, True,  False, False, True,  True,  False, False, False, False, False, False, False, False, True, False, True, False, False, False, False, False, False, False, False, False, False],
		# PI
		[False, False, False, False, True,  True,  False, False, False, True,  False, False, False, False, False, True,  False, False, False, False, False, False, False, False, False, False, True],
		# PR
		[False, False, False, False, False, False, False, False, False, False, False, True,  False, False, False, False, False, False, False, False, False, False, False,  True,  True,  False, False],
		# RJ
		[False, False, False, False, False, False, False, True,  False, False, True,  False, False, False, False, False, False, False, False, False, False, False, False, False,  True, False, False],
		# RN
		[False, False, False, False, False, True,  False, False, False, False, False, False, False, False, True,  False, False, False, False, False, False, False, False, False, False, False, False],
		# RO
		[True,  False, True,  False, False, False, False, False, False, False, False, False, True,  False, False, False, False, False, False, False, False, False, False, False, False, False, False],
		# RR
		[False, False, True,  False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False],
		# RS
		[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,  False, False, False, False, False, True,  False, False, False],
		# SC
		[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True,  False, False, False, False, True,  False, False, False, False],
		# SP
		[False, False, False, False, False, False, False, False, False, False, True,  True,  False, False, False, False, False, True,  True,  False, False, False, False, False, False, False, False],
		# SE
		[False, True,  False, False, True,  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
		# TO
		[False, False, False, False, True,  False, False, False, True,  True,  False, False, True,  True,  False, False, True, False, False, False, False, False, False, False, False, False, False],
	]

	@classmethod
	def print_matrix(cls):
		"""Gera uma visualização da matriz (0/1) usando matplotlib.

		Parâmetros opcionais (chamada: `MAdj.print_matrix(show=True, save_path=None)`):
		- show: se True, chama `plt.show()` para exibir a figura.
		- save_path: se fornecido, salva a figura nesse caminho (ex: 'matrix.png').
		Retorna a tupla `(fig, ax)` criada.
		"""

		

		n = len(cls.STATES)
		# Converter booleans para 0/1
		mat = [[1 if cell else 0 for cell in row] for row in cls.MATRIX]

		fig, ax = plt.subplots(figsize=(10, 10))
		cax = ax.imshow(mat, cmap='Greys', interpolation='nearest', vmin=0, vmax=1)

		# Configurar ticks com as siglas
		ax.set_xticks(range(n))
		ax.set_yticks(range(n))
		ax.set_xticklabels(cls.STATES, rotation=90)
		ax.set_yticklabels(cls.STATES)

		# Pequeno ajuste visual
		ax.set_xlabel('Estados')
		ax.set_ylabel('Estados')
		ax.set_title('Matriz de Fronteiras (1 = fronteira, 0 = não)')
		plt.tight_layout()

		# Retornar fig/ax para quem chamar; não forçar show/ save aqui
		return fig, ax

	@classmethod
	def calcular_graus(cls):
		graus = {}
		for i, estado in enumerate(cls.STATES):
			grau = sum(cls.MATRIX[i])
			graus[estado] = grau
		return graus


	@classmethod
	def listar_vizinhos(cls, estado):
		indice = cls.STATES.index(estado)
		vizinhos = []

		for j, eh_vizinho in enumerate(cls.MATRIX[indice]):
			if eh_vizinho:
				vizinhos.append(cls.STATES[j])

		return vizinhos

	@classmethod
	def estados_com_grau_maximo(cls):
		graus = cls.calcular_graus()
		maior_grau = max(graus.values())

		estados = []
		for estado, grau in graus.items():
			if grau == maior_grau:
				estados.append(estado)

		return maior_grau, estados

	@classmethod
	def estados_com_grau_minimo(cls):
		graus = cls.calcular_graus()
		menor_grau = min(graus.values())

		estados = []
		for estado, grau in graus.items():
			if grau == menor_grau:
				estados.append(estado)

		return menor_grau, estados

	@classmethod
	def frequencia_dos_graus(cls):
		graus = cls.calcular_graus()
		frequencia = {}

		for grau in graus.values():
			if grau not in frequencia:
				frequencia[grau] = 0
			frequencia[grau] += 1

		return frequencia

	@classmethod
	def plotar_histograma_graus(cls):
		graus = list(cls.calcular_graus().values())

		plt.figure(figsize=(8, 5))
		plt.hist(graus, bins=range(min(graus), max(graus) + 2), align='left',
				color='skyblue', edgecolor='black', rwidth=0.8)

		plt.xlabel('Grau')
		plt.ylabel('Frequência')
		plt.title('Histograma da Frequência dos Graus')
		plt.xticks(range(min(graus), max(graus) + 1))
		plt.grid(axis='y', linestyle='--', alpha=0.7)
		plt.tight_layout()
		plt.show()

	@classmethod
	def mostrar_resultados(cls):
		maior_grau, estados_max = cls.estados_com_grau_maximo()
		menor_grau, estados_min = cls.estados_com_grau_minimo()

		print('---------------------------------------------------------------------------------------')

		print('Estados com grau máximo:', maior_grau)
		for estado in estados_max:
			print(f'- {estado}: vizinhos = {cls.listar_vizinhos(estado)}')

		print('---------------------------------------------------------------------------------------')

		print('\nEstados com grau mínimo:', menor_grau)
		for estado in estados_min:
			print(f'- {estado}: vizinhos = {cls.listar_vizinhos(estado)}')

		print('---------------------------------------------------------------------------------------')

		print('\nFrequência dos graus:')
		frequencia = cls.frequencia_dos_graus()
		for grau in sorted(frequencia):
			print(f'Grau {grau}: {frequencia[grau]} estado(s)')

		print('---------------------------------------------------------------------------------------')



	


    