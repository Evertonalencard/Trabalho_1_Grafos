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
		[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True,  False, False, False, False, False, False, False, False, False, True,  False],
		# AM
		[True,  False, False, False, False, False, False, False, False, False, False, False, True,  True,  False, False, False, False, False, False, True,  True,  False, False, False, False, False],
		# AP
		[False, False, False, False, False, False, False, False, False, False, False, False, False, True,  False, False, False, False, False, False, False, False, False, False, False, False, False],
		# BA
		[False, True,  False, False, False, False, False, False, True,  False, True,  False, False, False, False, True,  True,  False, False, False, False, False, False, False, False, True,  True ],
		# CE
		[False, False, False, False, False, False, False, False, False, False, False, False, False, False, True,  True,  True,  False, False, True,  False, False, False, False, False, False, False],
		# DF
		[False, False, False, False, False, False, False, False, True,  False, True,  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
		# ES
		[False, False, False, False, False, False, False, False, False, False, True,  False, False, False, False, False, False, False, True,  False, False, False, False, False, False, False, False],
		# GO
		[False, False, False, False, True,  False, True,  False, False, False, True,  True,  True,  False, False, False, False, False, False, False, False, False, False, False, False, False, True ],
		# MA
		[False, False, False, False, False, False, False, False, False, False, False, False, False, True,  False, False, True,  False, False, False, False, False, False, False, False, False, True ],
		# MG
		[False, False, False, False, True,  False, True,  True,  True,  False, False, True,  False, False, False, False, False, False, True,  False, False, False, False, False, True,  False, False],
		# MS
		[False, False, False, False, False, False, False, False, True,  False, True,  False, True,  False, False, False, False, True,  False, False, False, False, False, False, True,  False, False],
		# MT
		[False, False, True,  False, False, False, False, False, True,  False, False, True,  False, True,  False, False, False, False, False, False, True,  False, False, False, False, False, True ],
		# PA
		[False, False, True,  True,  False, False, False, False, False, True,  False, False, True,  False, False, False, False, False, False, False, False, False, False, False, False, False, True ],
		# PB
		[False, False, False, False, False, True,  False, False, False, False, False, False, False, False, False, True,  False, False, False, True,  False, False, False, False, False, False, False],
		# PE
		[False, True,  False, False, True,  True,  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
		# PI
		[False, False, False, False, True,  True,  False, False, False, True,  False, False, False, False, False, True,  False, False, False, False, False, False, False, False, False, False, False],
		# PR
		[False, False, False, False, False, False, False, False, False, False, False, True,  False, False, False, False, False, False, False, False, False, False, True,  True,  True,  False, False],
		# RJ
		[False, False, False, False, False, False, False, True,  False, False, True,  False, False, False, False, False, False, False, False, False, False, False, False, True,  False, False, False],
		# RN
		[False, False, False, False, False, True,  False, False, False, False, False, False, False, False, True,  False, False, False, False, False, False, False, False, False, False, False, False],
		# RO
		[True,  False, True,  False, False, False, False, False, False, False, False, False, True,  False, False, False, False, False, False, False, False, False, False, False, False, False, False],
		# RR
		[False, False, True,  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
		# RS
		[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True,  False, False, False, False, False, True,  False, False, False],
		# SC
		[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True,  False, False, False, False, True,  False, False, False, False],
		# SP
		[False, False, False, False, False, False, False, False, False, False, True,  True,  False, False, False, False, False, True,  True,  False, False, False, False, False, False, False, False],
		# SE
		[False, True,  False, False, True,  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
		# TO
		[False, False, False, False, True,  False, False, False, True,  True,  False, False, True,  True,  False, False, False, False, False, False, False, False, False, False, False, False, False],
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


    