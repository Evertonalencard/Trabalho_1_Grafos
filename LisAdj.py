import math
import matplotlib.pyplot as plt

from MAdj import MAdj


class LisAdj:
    """Lista de Adjacência gerada a partir da matriz de MAdj."""

    @classmethod
    def gerar_lista(cls):
        """Constrói a lista de adjacência: {estado: [vizinhos]}"""
        lista = {}
        for i, estado in enumerate(MAdj.STATES):
            vizinhos = [MAdj.STATES[j] for j, eh_vizinho in enumerate(MAdj.MATRIX[i]) if eh_vizinho]
            lista[estado] = vizinhos
        return lista

    @classmethod
    def imprimir_lista(cls):
        lista = cls.gerar_lista()
        print('---------------------------------------------------------------------------------------')
        for estado, vizinhos in lista.items():
            print(f'{estado}: {vizinhos}')

        print('---------------------------------------------------------------------------------------')

    @classmethod
    def _calcular_posicoes(cls):
        """Distribui os estados em um círculo (layout circular manual)."""
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
        """Desenha o grafo da lista de adjacência usando apenas matplotlib."""
        lista = cls.gerar_lista()
        posicoes = cls._calcular_posicoes()

        fig, ax = plt.subplots(figsize=figsize)

        # Desenhar arestas (evitando duplicar, já que o grafo é não-direcionado)
        arestas_desenhadas = set()
        for estado, vizinhos in lista.items():
            x1, y1 = posicoes[estado]
            for vizinho in vizinhos:
                aresta = tuple(sorted([estado, vizinho]))
                if aresta in arestas_desenhadas:
                    continue
                arestas_desenhadas.add(aresta)
                x2, y2 = posicoes[vizinho]
                ax.plot([x1, x2], [y1, y2], color='gray', linewidth=0.8, zorder=1)

        # Desenhar nós (estados)
        for estado, (x, y) in posicoes.items():
            ax.scatter(x, y, s=600, color='skyblue', edgecolors='black', zorder=2)
            ax.text(x, y, estado, ha='center', va='center', fontsize=8, fontweight='bold', zorder=3)

        ax.set_title('Grafo de Adjacência - Estados Brasileiros')
        ax.set_aspect('equal')
        ax.axis('off')
        plt.tight_layout()

        return fig, ax