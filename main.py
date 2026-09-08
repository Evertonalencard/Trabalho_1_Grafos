import matplotlib
import matplotlib.pyplot as plt

from LisAdj import LisAdj	
from MAdj import MAdj
from LisIndexada import LisIndexada
from TeoCores.ConfigUF import carregar_geodataframe
from TeoCores.front import  MapaBrasil


if __name__ == '__main__':
    gdf = carregar_geodataframe()
    
    colorador = ColoradorDeEstados(gdf)
    cores_por_estado = colorador.calcular_cores()
    
    mapa = MapaBrasil(gdf)
    mapa.plotar(
        cores_por_estado,
        titulo="Estados do Brasil - 4 cores, sem vizinhos repetidos",
        caminho_saida="mapa_brasil_geopandas_classes.png",
    )
	
	# # salvar imagem e mostrar
	# fig, ax = MAdj.print_matrix()
	# fig.savefig('matriz_fronteiras.png', dpi=200)
	# plt.show()

	# #mostra grau maximo, minimo e vizinhos
	# MAdj.mostrar_resultados()

	# # Mostra histograma da frequência dos graus
	# MAdj.plotar_histograma_graus()

	# # salvar imagem e mostrar da lista de adjacência
	# LisAdj.imprimir_lista()
	# fig,ax = LisAdj.desenhar_grafo()
	# fig.savefig('Lista_Adjacência.png', dpi=200)
	# plt.show()

	# #mostra grau maximo, minimo e vizinhos da lista de adjacência
	# LisAdj.mostrar_resultados()
	# LisAdj.plotar_histograma_graus()

	# LisIndexada.imprimir_lista_indexada()
	# fig, ax = LisIndexada.plotar_tabelas()
	# fig.savefig('Lista_Indexada.png', dpi=200)
	# plt.show()
	# LisIndexada.plotar_histograma_graus()


	# LisIndexada.gerar_tabelas()
		



