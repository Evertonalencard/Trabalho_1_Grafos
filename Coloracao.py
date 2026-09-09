import math

import matplotlib.pyplot as plt

from MAdj import MAdj
from LisAdj import LisAdj


class Coloracao:
	"""Coloração de grafos com algoritmo guloso (heurística de Welsh-Powell).

	O Teorema das Quatro Cores garante que qualquer mapa planar pode ser
	colorido com no máximo 4 cores, de forma que regiões vizinhas nunca
	compartilhem a mesma cor. Encontrar essa coloração ótima é um problema
	computacionalmente difícil (NP-completo em geral), então aqui usamos uma
	heurística gulosa: Welsh-Powell.

	Ideia do algoritmo:
	1. Ordena os vértices (estados) em ordem decrescente de grau (nº de
	   vizinhos) — estados mais "problemáticos" (com mais fronteiras) são
	   coloridos primeiro, quando ainda há mais cores livres.
	2. Para cada estado, na ordem definida, atribui a MENOR cor (dentre as
	   disponíveis) que nenhum de seus vizinhos já coloridos esteja usando.
	3. Se as 4 cores não bastarem para algum vértice (o que não deveria
	   ocorrer em um grafo planar bem formado), uma 5ª cor é usada como
	   segurança, para nunca quebrar a restrição de vizinhos com cores
	   diferentes.
	"""

	NOMES_CORES = ['Vermelho', 'Verde', 'Azul', 'Amarelo', 'Roxo (extra)']
	CORES_HEX = ['#e74c3c', '#2ecc71', '#3498db', '#f1c40f', '#9b59b6']

	# ---------------------------- Algoritmo guloso ----------------------------

	@classmethod
	def colorir_welsh_powell(cls, max_cores=4):
		"""Executa o algoritmo guloso de Welsh-Powell.

		Retorna um dicionário {estado: indice_da_cor}, onde indice_da_cor é
		0, 1, 2 ou 3 (correspondendo a NOMES_CORES / CORES_HEX).
		"""
		vetor_vertices = LisAdj.gerar_lista()

		# 1) ordena por grau decrescente (desempate: ordem alfabética, para
		#    o resultado ser determinístico e reprodutível)
		ordenados = sorted(
			vetor_vertices,
			key=lambda v: (-len(v.vizinhos), v.estado)
		)

		cor_do_estado = {}

		for vertice in ordenados:
			cores_usadas_pelos_vizinhos = {
				cor_do_estado[vizinho]
				for vizinho in vertice.vizinhos
				if vizinho in cor_do_estado
			}

			cor_escolhida = None
			for indice_cor in range(max_cores):
				if indice_cor not in cores_usadas_pelos_vizinhos:
					cor_escolhida = indice_cor
					break

			if cor_escolhida is None:
				# Segurança: não deveria acontecer em um grafo planar com
				# max_cores=4, mas evita que o algoritmo quebre a restrição.
				cor_escolhida = max(cores_usadas_pelos_vizinhos, default=-1) + 1

			cor_do_estado[vertice.estado] = cor_escolhida

		return cor_do_estado

	# ---------------------------- Saída para o front-end ----------------------------

	@classmethod
	def obter_cores_hex(cls, cor_do_estado=None):
		"""Retorna o resultado no formato que o front-end precisa: um
		dicionário {estado (str): cor_hexadecimal (str)}.

		Exemplo de retorno:
			{'AC': '#e74c3c', 'AL': '#3498db', 'AM': '#3498db', ...}
		"""
		cor_do_estado = cor_do_estado or cls.colorir_welsh_powell()
		return {
			estado: cls.CORES_HEX[indice_cor]
			for estado, indice_cor in cor_do_estado.items()
		}

	# ---------------------------- Validação ----------------------------

	@classmethod
	def validar_coloracao(cls, cor_do_estado):
		"""Confere se algum par de estados vizinhos ficou com a mesma cor.

		Retorna uma lista de pares (estado_a, estado_b) em conflito.
		Lista vazia = coloração válida.
		"""
		MAdj._garantir_dados_carregados()
		conflitos = []
		n = len(MAdj.STATES)
		for i in range(n):
			for j in range(i + 1, n):
				if MAdj.MATRIX[i][j]:
					estado_a, estado_b = MAdj.STATES[i], MAdj.STATES[j]
					if cor_do_estado.get(estado_a) == cor_do_estado.get(estado_b):
						conflitos.append((estado_a, estado_b))
		return conflitos

	# ---------------------------- Relatório em texto ----------------------------

	@classmethod
	def imprimir_coloracao(cls, cor_do_estado=None):
		cor_do_estado = cor_do_estado or cls.colorir_welsh_powell()
		qtd_cores_usadas = len(set(cor_do_estado.values()))

		print('---------------------------------------------------------------------------------------')
		print(f'Coloração gulosa (Welsh-Powell) — {qtd_cores_usadas} cor(es) utilizada(s)')
		print('---------------------------------------------------------------------------------------')

		por_cor = {}
		for estado, indice_cor in sorted(cor_do_estado.items()):
			por_cor.setdefault(indice_cor, []).append(estado)

		for indice_cor in sorted(por_cor):
			nome_cor = cls.NOMES_CORES[indice_cor]
			print(f'{nome_cor}: {", ".join(por_cor[indice_cor])}')

		conflitos = cls.validar_coloracao(cor_do_estado)
		print('---------------------------------------------------------------------------------------')
		if conflitos:
			print(f'ATENÇÃO: {len(conflitos)} par(es) de vizinhos com a mesma cor:')
			for a, b in conflitos:
				print(f'  - {a} e {b}')
		else:
			print('Coloração válida: nenhum par de estados vizinhos compartilha a mesma cor.')
		print('---------------------------------------------------------------------------------------')

		return cor_do_estado

	# ---------------------------- Visualização ----------------------------

	@classmethod
	def _calcular_posicoes(cls):
		n = len(MAdj.STATES)
		posicoes = {}
		for i, estado in enumerate(MAdj.STATES):
			angulo = 2 * math.pi * i / n
			posicoes[estado] = (math.cos(angulo), math.sin(angulo))
		return posicoes

	@classmethod
	def desenhar_grafo_colorido(cls, cor_do_estado=None, figsize=(10, 10)):
		"""Desenha o grafo de fronteiras com os vértices pintados conforme
		a coloração calculada."""
		MAdj._garantir_dados_carregados()
		cor_do_estado = cor_do_estado or cls.colorir_welsh_powell()

		vetor_vertices = LisAdj.gerar_lista()
		posicoes = cls._calcular_posicoes()

		fig, ax = plt.subplots(figsize=figsize)

		arestas_desenhadas = set()
		for vertice in vetor_vertices:
			x1, y1 = posicoes[vertice.estado]
			for vizinho in vertice.vizinhos:
				aresta = tuple(sorted([vertice.estado, vizinho]))
				if aresta in arestas_desenhadas:
					continue
				arestas_desenhadas.add(aresta)
				x2, y2 = posicoes[vizinho]
				ax.plot([x1, x2], [y1, y2], color='gray', linewidth=0.8, zorder=1)

		for estado, (x, y) in posicoes.items():
			indice_cor = cor_do_estado.get(estado, 0)
			ax.scatter(x, y, s=650, color=cls.CORES_HEX[indice_cor], edgecolors='black', zorder=2)
			ax.text(x, y, estado, ha='center', va='center', fontsize=8, fontweight='bold', zorder=3)

		qtd_cores_usadas = len(set(cor_do_estado.values()))
		ax.set_title(f'Coloração de Mapa (Teorema das 4 Cores) — {qtd_cores_usadas} cor(es)')
		ax.set_aspect('equal')
		ax.axis('off')
		plt.tight_layout()

		return fig, ax