import matplotlib
import matplotlib.pyplot as plt

from LisAdj import LisAdj	
from MAdj import MAdj


if __name__ == '__main__':
	# salvar imagem e mostrar
	fig, ax = MAdj.print_matrix()
	fig.savefig('matriz_fronteiras.png', dpi=200)
	plt.show()

	#mostra grau maximo, minimo e vizinhos
	MAdj.mostrar_resultados()

	# Mostra histograma da frequência dos graus
	MAdj.plotar_histograma_graus()

	LisAdj.imprimir_lista()
	fig,ax = LisAdj.desenhar_grafo()
	fig.savefig('Lista_Adjacência.png', dpi=200)
	plt.show()

