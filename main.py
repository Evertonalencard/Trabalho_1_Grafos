import matplotlib
import matplotlib.pyplot as plt

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

