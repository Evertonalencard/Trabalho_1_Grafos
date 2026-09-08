
import geopandas as gpd
import matplotlib.pyplot as plt
import networkx as nx

class MapaBrasil:
    
    def __init__(self, gdf: gpd.GeoDataFrame):
        self.gdf = gdf
        
    def plotar(self, cores_por_estado: dict, titulo: str = "Mapa do Brasil", caminho_saida: str = "mapa_brasil.png"):
        gdf_plot = self.gdf.copy()
        gdf_plot["cor"] = gdf_plot.index.map(cores_por_estado)
        
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