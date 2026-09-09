import matplotlib.pyplot as plt

from MAdj import MAdj
from LisAdj import LisAdj
from LisIndexada import LisIndexada
from Coloracao import Coloracao
from TeoCores.front import exibir_mapa_colorido


if __name__ == '__main__':
	# ---------------------------------------------------------------
	# 0) Entrada de dados: carrega estados e fronteiras de um CSV
	#    (arquivo de arestas, ver fronteiras.csv). Troque o caminho
	#    abaixo para usar outro arquivo de entrada.
	# ---------------------------------------------------------------
	MAdj.carregar_dados('fronteiras.csv')
	print(f'{len(MAdj.STATES)} estados carregados: {MAdj.STATES}')

	# ---------------------------------------------------------------
	# 1) Matriz de adjacência
	# ---------------------------------------------------------------
	fig, ax = MAdj.print_matrix()
	fig.savefig('matriz_fronteiras.png', dpi=200)
	plt.close(fig)

	MAdj.mostrar_resultados()
	# MAdj.plotar_histograma_graus()  # abre uma janela interativa

	# ---------------------------------------------------------------
	# 2) Lista de adjacência
	# ---------------------------------------------------------------
	LisAdj.imprimir_lista()
	fig, ax = LisAdj.desenhar_grafo()
	fig.savefig('Lista_Adjacência.png', dpi=200)
	plt.close(fig)

	LisAdj.mostrar_resultados()
	# LisAdj.plotar_histograma_graus()  # abre uma janela interativa

	# ---------------------------------------------------------------
	# 3) Lista indexada (tabelas alfa e beta)
	# ---------------------------------------------------------------
	LisIndexada.imprimir_lista_indexada()
	fig, (ax_tabelas, ax_grafo) = LisIndexada.plotar_tabelas()
	fig.savefig('Lista_Indexada.png', dpi=200)
	plt.close(fig)
	# LisIndexada.plotar_histograma_graus()  # abre uma janela interativa

	# ---------------------------------------------------------------
	# 4) Coloração de mapa (Teorema das 4 cores) — algoritmo guloso
	# ---------------------------------------------------------------
	cor_do_estado = Coloracao.imprimir_coloracao()
	fig, ax = Coloracao.desenhar_grafo_colorido(cor_do_estado)
	fig.savefig('Coloracao_4_Cores.png', dpi=200)
	plt.close(fig)

	# Dicionário {estado: cor_hex} para entregar ao front-end
	cores_hex_por_estado = Coloracao.obter_cores_hex(cor_do_estado)
	print('\nDicionário para o front-end (estado -> cor hexadecimal):')
	print(cores_hex_por_estado)


	print('\nArquivos gerados: matriz_fronteiras.png, Lista_Adjacência.png, '
		  'Lista_Indexada.png, Coloracao_4_Cores.png')
 
	exibir_mapa_colorido()
 
 
 