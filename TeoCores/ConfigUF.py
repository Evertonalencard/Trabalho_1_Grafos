import json
import urllib.request

import geopandas as gpd


NAME_TO_UF = {
    "Acre": "AC", "Alagoas": "AL", "Amapá": "AP", "Amazonas": "AM",
    "Bahia": "BA", "Ceará": "CE", "Distrito Federal": "DF",
    "Espírito Santo": "ES", "Goiás": "GO", "Maranhão": "MA",
    "Mato Grosso": "MT", "Mato Grosso do Sul": "MS", "Minas Gerais": "MG",
    "Pará": "PA", "Paraíba": "PB", "Paraná": "PR", "Pernambuco": "PE",
    "Piauí": "PI", "Rio de Janeiro": "RJ", "Rio Grande do Norte": "RN",
    "Rio Grande do Sul": "RS", "Rondônia": "RO", "Roraima": "RR",
    "Santa Catarina": "SC", "São Paulo": "SP", "Sergipe": "SE",
    "Tocantins": "TO",
}

GEOJSON_URL = (
    "https://raw.githubusercontent.com/giuliano-macedo/"
    "geodata-br-states/main/geojson/br_states.json"
)

def carregar_geodataframe() -> gpd.GeoDataFrame:
    try:
        gdf = gpd.read_file(GEOJSON_URL)
    except Exception:
        with urllib.request.urlopen(GEOJSON_URL) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        gdf = gpd.GeoDataFrame.from_features(data["features"])

    name_col = "name" if "name" in gdf.columns else "Estado" if "Estado" in gdf.columns else gdf.columns[0]
    gdf["UF"] = gdf[name_col].map(NAME_TO_UF)
    gdf = gdf.dropna(subset=["UF"]).set_index("UF")
    return gdf