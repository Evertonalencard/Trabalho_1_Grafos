import matplotlib
import matplotlib.pyplot as plt

from MAdj import MAdj


if __name__ == '__main__':
	fig, ax = MAdj.print_matrix()
	# salvar imagem e mostrar
	fig.savefig('matriz_fronteiras.png', dpi=200)
	import matplotlib.pyplot as plt
	plt.show()

