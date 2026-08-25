import math

import matplotlib.pyplot as plt

from MAdj import MAdj


class LisIndexada:
	"""Lista indexada do grafo, formada pelas tabelas alfa e beta.

	Alfa guarda a primeira posição dos vizinhos de cada estado em beta.
	Beta guarda os vizinhos em sequência. Os índices das duas tabelas
	começam em 1, como no modelo apresentado na captura.
	"""

	@classmethod
	def gerar_tabelas(cls):
		"""Retorna as tabelas alfa e beta construídas a partir da matriz."""
		alfa = []
		beta = []
		proxima_posicao = 1

		for linha in MAdj.MATRIX:
			alfa.append(proxima_posicao)
			for indice, eh_vizinho in enumerate(linha):
				if eh_vizinho:
					beta.append(MAdj.STATES[indice])
					proxima_posicao += 1

		return alfa, beta

	@classmethod
	def gerar_lista_indexada(cls):
		"""Retorna alfa e beta com os índices explícitos para consulta."""
		alfa, beta = cls.gerar_tabelas()
		return {
			'alfa': {i + 1: posicao for i, posicao in enumerate(alfa)},
			'beta': {i + 1: estado for i, estado in enumerate(beta)},
		}

	@classmethod
	def listar_vizinhos(cls, estado):
		"""Lista os vizinhos de um estado usando as tabelas alfa e beta."""
		if estado not in MAdj.STATES:
			return []

		indice_estado = MAdj.STATES.index(estado)
		alfa, beta = cls.gerar_tabelas()
		inicio = alfa[indice_estado] - 1
		fim = alfa[indice_estado + 1] - 1 if indice_estado + 1 < len(alfa) else len(beta)
		return beta[inicio:fim]

	@classmethod
	def calcular_graus(cls):
		return {estado: len(cls.listar_vizinhos(estado)) for estado in MAdj.STATES}

	@classmethod
	def estados_com_grau_maximo(cls):
		graus = cls.calcular_graus()
		maior_grau = max(graus.values())
		return maior_grau, [estado for estado, grau in graus.items() if grau == maior_grau]

	@classmethod
	def estados_com_grau_minimo(cls):
		graus = cls.calcular_graus()
		menor_grau = min(graus.values())
		return menor_grau, [estado for estado, grau in graus.items() if grau == menor_grau]

	@classmethod
	def frequencia_dos_graus(cls):
		frequencia = {}
		for grau in cls.calcular_graus().values():
			frequencia[grau] = frequencia.get(grau, 0) + 1
		return frequencia

	@classmethod
	def imprimir_lista_indexada(cls):
		print('---------------------------------------------------------------------------------------')
		alfa, beta = cls.gerar_tabelas()

		print('\nLista indexada')
		print('Alfa:')
		print('  valor   :', ' '.join(f'{valor:>3}' for valor in alfa))
		print('Beta:')
		print('  valor   :', ' '.join(f'{valor:>3}' for valor in beta))

		maior_grau, estados_max = cls.estados_com_grau_maximo()
		menor_grau, estados_min = cls.estados_com_grau_minimo()
		print('---------------------------------------------------------------------------------------')
		print(f'\nGrau máximo: {maior_grau}')
		for estado in estados_max:
			print(f'- {estado}: vizinhos = {cls.listar_vizinhos(estado)}')
		print('---------------------------------------------------------------------------------------')
		print(f'Grau mínimo: {menor_grau}')
		for estado in estados_min:
			print(f'- {estado}: vizinhos = {cls.listar_vizinhos(estado)}')
		print('---------------------------------------------------------------------------------------')
		print('Frequência dos graus:', cls.frequencia_dos_graus())
		print('---------------------------------------------------------------------------------------')

	@classmethod
	def plotar_tabelas(cls, figsize=(14, 7)):
		"""Mostra as tabelas alfa e beta e o grafo correspondente."""
		alfa, beta = cls.gerar_tabelas()
		fig, (ax_tabelas, ax_grafo) = plt.subplots(1, 2, figsize=figsize)

		ax_tabelas.axis('off')
		tabela_alfa = ax_tabelas.table(
			cellText=[
				['Posicao', *range(1, len(alfa) + 1)],
				['Alfa', *alfa],
			],
			loc='upper center',
			cellLoc='center',
		)
		tabela_alfa.auto_set_font_size(False)
		tabela_alfa.set_fontsize(7)
		tabela_alfa.scale(1, 1.8)

		tabela_beta = ax_tabelas.table(
			cellText=[
				['Posicao', *range(1, len(beta) + 1)],
				['Beta', *beta],
			],
			loc='lower center',
			cellLoc='center',
		)
		tabela_beta.auto_set_font_size(False)
		tabela_beta.set_fontsize(6)
		tabela_beta.scale(1, 1.8)
		ax_tabelas.set_title('Lista indexada: tabelas alfa e beta')

		posicoes = {}
		quantidade = len(MAdj.STATES)
		for indice, estado in enumerate(MAdj.STATES):
			angulo = 2 * math.pi * indice / quantidade
			posicoes[estado] = (1.1 * math.cos(angulo), 1.1 * math.sin(angulo))

		arestas = set()
		for estado in MAdj.STATES:
			for vizinho in cls.listar_vizinhos(estado):
				aresta = tuple(sorted((estado, vizinho)))
				if aresta not in arestas:
					arestas.add(aresta)
					x1, y1 = posicoes[estado]
					x2, y2 = posicoes[vizinho]
					ax_grafo.plot([x1, x2], [y1, y2], color='gray', linewidth=0.7)

		for estado, (x, y) in posicoes.items():
			ax_grafo.scatter(x, y, s=500, color='lightgreen', edgecolors='black')
			ax_grafo.text(x, y, estado, ha='center', va='center', fontsize=8, fontweight='bold')

		ax_grafo.set_title('Grafo de fronteiras')
		ax_grafo.set_aspect('equal')
		ax_grafo.axis('off')
		fig.tight_layout()
		return fig, (ax_tabelas, ax_grafo)

	@classmethod
	def plotar_histograma_graus(cls):
		graus = list(cls.calcular_graus().values())
		fig, ax = plt.subplots(figsize=(8, 5))
		ax.hist(graus, bins=range(min(graus), max(graus) + 2), align='left',
				color='lightgreen', edgecolor='black', rwidth=0.8)
		ax.set_xlabel('Grau')
		ax.set_ylabel('Quantidade de estados')
		ax.set_title('Frequência dos graus - lista indexada')
		ax.set_xticks(range(min(graus), max(graus) + 1))
		ax.grid(axis='y', linestyle='--', alpha=0.7)
		fig.tight_layout()
		plt.show()
		return fig, ax
