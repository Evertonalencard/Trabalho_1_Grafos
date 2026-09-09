
import geopandas as gpd
import matplotlib.pyplot as plt

from Coloracao import Coloracao
from MAdj import MAdj
from TeoCores.ConfigUF import carregar_geodataframe

class MapaBrasil:
    
    def __init__(self, gdf: gpd.GeoDataFrame):
        self.gdf = gdf
        
    def plotar(self, cores_por_estado: dict, titulo: str = "Mapa do Brasil", caminho_saida: str = "mapa_brasil.png"):
        gdf_plot = self.gdf.copy()
        gdf_plot["cor"] = gdf_plot.index.to_series().map(cores_por_estado)
        
        if gdf_plot["cor"].isna().any():
            faltando = gdf_plot[gdf_plot["cor"].isna()].index.tolist()
            raise ValueError(f"Faltam cores para os estados: {faltando}")
        
        fig, ax = plt.subplots(figsize=(10, 10))
        gdf_plot.plot(color=gdf_plot["cor"], edgecolor="black", linewidth=0.6, ax=ax)
        
        for uf, geom in gdf_plot.geometry.items():
            c = geom.centroid
            ax.annotate(uf, (c.x, c.y), ha="center", fontsize=8, fontweight="bold")
            
        ax.set_title(titulo)
        ax.axis("off")
        plt.tight_layout()
        plt.savefig(caminho_saida, dpi=150, bbox_inches="tight")
        plt.show()


def exibir_mapa_colorido(caminho_csv: str = "fronteiras.csv", caminho_saida: str = "mapa_brasil.png"):
    """Calcula as cores e exibe o mapa do Brasil usando GeoPandas."""
    MAdj.carregar_dados(caminho_csv)
    estado_e_cor = Coloracao.obter_estado_e_cor()
    mapa = MapaBrasil(carregar_geodataframe())
    mapa.plotar(estado_e_cor, caminho_saida=caminho_saida)
    return estado_e_cor


