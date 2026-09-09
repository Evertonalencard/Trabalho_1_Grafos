import math
import matplotlib.pyplot as plt

from MAdj import MAdj


class Vertice:
    """Representa um vértice do grafo: um ID, o estado e sua lista de vizinhos."""

    def __init__(self, id_vertice, estado):
        self.id = id_vertice
        self.estado = estado
        self.vizinhos = []  # lista encadeada (ArrayList) de vértices adjacentes

    def adicionar_vizinho(self, estado_vizinho):
        self.vizinhos.append(estado_vizinho)

    def __repr__(self):
        return f'Vertice(id={self.id}, estado={self.estado}, vizinhos={self.vizinhos})'


class LisAdj:
    """Lista de Adjacência gerada a partir da matriz de MAdj.

    Estrutura:
    - Vetor de tamanho 27 (posições 0 a 26)
    - Cada posição do vetor guarda um objeto Vertice
    - Cada Vertice tem: id, estado (nome) e uma lista de vizinhos
    """

    @classmethod
    def gerar_lista(cls):
        """Constrói o vetor de vértices, cada um com ID e lista de vizinhos."""
        MAdj._garantir_dados_carregados()
        n = len(MAdj.STATES)
        vetor_vertices = [None] * n  # vetor de tamanho 27

        for i in range(n):
            vetor_vertices[i] = Vertice(id_vertice=i, estado=MAdj.STATES[i])

        for i in range(n):
            for j, eh_vizinho in enumerate(MAdj.MATRIX[i]):
                if eh_vizinho:
                    vetor_vertices[i].adicionar_vizinho(MAdj.STATES[j])

        return vetor_vertices

    @classmethod
    def imprimir_lista(cls):
        print('---------------------------------------------------------------------------------------')
        vetor_vertices = cls.gerar_lista()
        for vertice in vetor_vertices:
            vizinhos_str = ' ---> '.join(vertice.vizinhos) if vertice.vizinhos else '(sem vizinhos)'
            print(f'[{vertice.id}] {vertice.estado} ---> {vizinhos_str}')

        print('---------------------------------------------------------------------------------------')

    @classmethod
    def _calcular_posicoes(cls):
        n = len(MAdj.STATES)
        posicoes = {}
        for i, estado in enumerate(MAdj.STATES):
            angulo = 2 * math.pi * i / n
            x = math.cos(angulo)
            y = math.sin(angulo)
            posicoes[estado] = (x, y)
        return posicoes

    @classmethod
    def desenhar_grafo(cls, figsize=(10, 10)):
        vetor_vertices = cls.gerar_lista()
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
            ax.scatter(x, y, s=600, color='skyblue', edgecolors='black', zorder=2)
            ax.text(x, y, estado, ha='center', va='center', fontsize=8, fontweight='bold', zorder=3)

        ax.set_title('Grafo de Adjacência - Estados Brasileiros')
        ax.set_aspect('equal')
        ax.axis('off')
        plt.tight_layout()

        return fig, ax

      # ---------- Análise de graus (a partir da lista de adjacência) ----------

    @classmethod
    def calcular_graus(cls):
        """Retorna {estado: grau}, onde grau = tamanho da lista de vizinhos."""
        vetor_vertices = cls.gerar_lista()
        graus = {}
        for vertice in vetor_vertices:
            graus[vertice.estado] = len(vertice.vizinhos)
        return graus

    @classmethod
    def listar_vizinhos(cls, estado):
        vetor_vertices = cls.gerar_lista()
        for vertice in vetor_vertices:
            if vertice.estado == estado:
                return vertice.vizinhos
        return []

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
                  color='lightgreen', edgecolor='black', rwidth=0.8)

        plt.xlabel('Grau')
        plt.ylabel('Frequência')
        plt.title('Histograma da Frequência dos Graus (Lista de Adjacência)')
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