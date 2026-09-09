import csv
import os

import matplotlib.pyplot as plt


class MAdj:
	"""Matriz de adjacência booleana entre unidades da federação.

	Diferente da versão anterior (matriz fixa no código), os dados agora
	são carregados de um arquivo de entrada (CSV de arestas). Basta chamar
	`MAdj.carregar_dados(caminho)` antes de usar as demais funcionalidades.

	Formato esperado do CSV (com ou sem cabeçalho):
		estado_origem,estado_destino
		AC,AM
		AC,RO
		AL,BA
		...

	Cada linha representa uma fronteira (aresta não-direcionada) entre dois
	estados. A lista de estados (STATES) é inferida automaticamente a
	partir dos códigos que aparecem no arquivo, em ordem alfabética.
	"""

	STATES = []
	MATRIX = []

	CAMINHO_PADRAO = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fronteiras.csv')

	# ---------------------------- Entrada de dados ----------------------------

	# Palavras que, se aparecerem na primeira linha, indicam que ela é um
	# cabeçalho (e não um par de vértices/estados de verdade). A lista é
	# ampla de propósito, para reconhecer nomes de coluna variados
	# ('estado_origem', 'regiao_origem', 'source', 'from', 'uf1' etc.).
	PALAVRAS_CABECALHO = (
		'origem', 'destino', 'from', 'to', 'source', 'target',
		'estado', 'regiao', 'região', 'uf', 'vertice', 'vértice', 'vertex',
		'node', 'pais', 'país', 'municipio', 'município', 'cidade', 'no1', 'no2',
	)

	@classmethod
	def carregar_dados(cls, caminho_csv=None, tem_cabecalho=None):
		"""Lê o arquivo CSV de fronteiras e monta STATES e MATRIX.

		Aceita QUALQUER csv de arestas com 2 colunas (nome do vértice de
		origem, nome do vértice de destino) — não precisa ser sobre estados
		brasileiros nem ter esses nomes de coluna específicos.

		Parâmetros:
		- caminho_csv: caminho do arquivo .csv. Se omitido, usa 'fronteiras.csv'
		  na mesma pasta deste módulo.
		- tem_cabecalho: True força ignorar a 1ª linha, False força tratá-la
		  como dado. Se None (padrão), tenta detectar automaticamente pelas
		  palavras em PALAVRAS_CABECALHO; se não reconhecer nada, assume que
		  NÃO há cabeçalho (mais seguro: não perde nenhuma aresta real).

		Retorna a tupla (STATES, MATRIX).
		"""
		caminho_csv = caminho_csv or cls.CAMINHO_PADRAO

		if not os.path.isfile(caminho_csv):
			raise FileNotFoundError(
				f"Arquivo de entrada não encontrado: '{caminho_csv}'. "
				"Informe o caminho de um CSV com 2 colunas (origem, destino)."
			)

		arestas = []
		estados = []

		with open(caminho_csv, newline='', encoding='utf-8') as f:
			linhas = list(csv.reader(f))

		if not linhas:
			raise ValueError(f"Arquivo '{caminho_csv}' está vazio.")

		if tem_cabecalho is None:
			primeira = ' '.join(c.strip().lower() for c in linhas[0])
			tem_cabecalho = any(palavra in primeira for palavra in cls.PALAVRAS_CABECALHO)

		inicio = 1 if tem_cabecalho else 0

		for numero_linha, linha in enumerate(linhas[inicio:], start=inicio + 1):
			linha = [c.strip() for c in linha if c.strip() != '']
			if not linha:
				continue  # ignora linhas em branco
			if len(linha) < 2:
				raise ValueError(
					f"Linha {numero_linha} do CSV é inválida (esperado 2 colunas): {linha}"
				)

			origem, destino = linha[0].upper(), linha[1].upper()

			if origem == destino:
				raise ValueError(f"Linha {numero_linha}: um estado não pode fazer fronteira consigo mesmo ({origem}).")

			arestas.append((origem, destino))
			if origem not in estados:
				estados.append(origem)
			if destino not in estados:
				estados.append(destino)

		estados.sort()
		indice = {estado: i for i, estado in enumerate(estados)}
		n = len(estados)
		matriz = [[False] * n for _ in range(n)]

		for origem, destino in arestas:
			i, j = indice[origem], indice[destino]
			matriz[i][j] = True
			matriz[j][i] = True

		cls.STATES = estados
		cls.MATRIX = matriz

		return cls.STATES, cls.MATRIX

	@classmethod
	def _garantir_dados_carregados(cls):
		if not cls.STATES or not cls.MATRIX:
			cls.carregar_dados()

	# ---------------------------- Visualização ----------------------------

	@classmethod
	def print_matrix(cls):
		"""Gera uma visualização da matriz (0/1) usando matplotlib.

		Retorna a tupla `(fig, ax)` criada.
		"""
		cls._garantir_dados_carregados()

		n = len(cls.STATES)
		mat = [[1 if cell else 0 for cell in row] for row in cls.MATRIX]

		fig, ax = plt.subplots(figsize=(10, 10))
		ax.imshow(mat, cmap='Greys', interpolation='nearest', vmin=0, vmax=1)

		ax.set_xticks(range(n))
		ax.set_yticks(range(n))
		ax.set_xticklabels(cls.STATES, rotation=90)
		ax.set_yticklabels(cls.STATES)

		ax.set_xlabel('Estados')
		ax.set_ylabel('Estados')
		ax.set_title('Matriz de Fronteiras (1 = fronteira, 0 = não)')
		plt.tight_layout()

		return fig, ax

	# ---------------------------- Análise de graus ----------------------------

	@classmethod
	def calcular_graus(cls):
		cls._garantir_dados_carregados()
		graus = {}
		for i, estado in enumerate(cls.STATES):
			graus[estado] = sum(cls.MATRIX[i])
		return graus

	@classmethod
	def listar_vizinhos(cls, estado):
		cls._garantir_dados_carregados()
		indice = cls.STATES.index(estado)
		return [cls.STATES[j] for j, eh_vizinho in enumerate(cls.MATRIX[indice]) if eh_vizinho]

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
		graus = cls.calcular_graus()
		frequencia = {}
		for grau in graus.values():
			frequencia[grau] = frequencia.get(grau, 0) + 1
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