import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from shapely.geometry import Point

gdf = gpd.read_file('municipios/areas_geoestadisticas_municipales.shp')
print(gdf.columns)
gdf['Key'] = gdf['CVE_ENT'] + gdf['CVE_MUN']

rezago = pd.read_csv("rezago_social/rezago_social.csv")
rezago_social = rezago[["lgc00_15cl3", "Key", "POB_TOTAL", "LAT", "LON"]]
rezago_social['Key'] = rezago_social['Key'].astype(str).str.zfill(5)

gdf = gdf.merge(rezago_social, on='Key')

crs = gdf.crs
geometry = [Point(xy) for xy in zip(gdf.LON, gdf.LAT)]
centers = gpd.GeoDataFrame(crs={'init': 'epsg:4326'}, geometry=geometry)
centers = centers.to_crs(crs)
print(centers)

legend_elements = [Line2D([0], [0], marker='o', color='w', label='Alto',
                          markerfacecolor='r', markersize=15),
                   Line2D([0], [0], marker='o', color='w', label='Medio',
                          markerfacecolor='yellow', markersize=15),
                   Line2D([0], [0], marker='o', color='w', label='Bajo',
                          markerfacecolor='g', markersize=15)]


colors = {1: 'green', 2: 'yellow', 3: 'red'}
fig, ax = plt.subplots()
gdf.plot(ax=ax, color=gdf['lgc00_15cl3'].map(colors), legend=True)
# centers.plot(ax=ax, column='capital', marker='*', markersize=1, color='black')
plt.axis('off')
plt.title("Mapa de Rezago Social a nivel municipal, 2015.")
txt = "Construido de acuerdo a las categorías de Rezago Social sugeridas por Vargas-Chanes y Valdez-Cruz (2017)."
plt.figtext(0.01, 0.01, txt, wrap=True, horizontalalignment='left', fontsize=12)
plt.legend(handles=legend_elements)
plt.show()
