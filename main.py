import matplotlib
import matplotlib.pyplot as plt

from LisAdj import LisAdj	
from MAdj import MAdj
from LisIndexada import LisIndexada


if __name__ == '__main__':
	# salvar imagem e mostrar
	fig, ax = MAdj.print_matrix()
	fig.savefig('matriz_fronteiras.png', dpi=200)
	plt.show()

	#mostra grau maximo, minimo e vizinhos
	MAdj.mostrar_resultados()

	# Mostra histograma da frequência dos graus
	MAdj.plotar_histograma_graus()

	# salvar imagem e mostrar da lista de adjacência
	LisAdj.imprimir_lista()
	fig,ax = LisAdj.desenhar_grafo()
	fig.savefig('Lista_Adjacência.png', dpi=200)
	plt.show()

	#mostra grau maximo, minimo e vizinhos da lista de adjacência
	LisAdj.mostrar_resultados()
	LisAdj.plotar_histograma_graus()

	LisIndexada.imprimir_lista_indexada()
	fig, ax = LisIndexada.plotar_tabelas()
	fig.savefig('Lista_Indexada.png', dpi=200)
	plt.show()
	LisIndexada.plotar_histograma_graus()



