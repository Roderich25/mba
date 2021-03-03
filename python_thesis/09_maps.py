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

csfont = {'fontname': 'Times New Roman'}
colors = {1: 'green', 2: 'yellow', 3: 'red'}
fig, (ax1, ax2) = plt.subplots(1, 2)
gdf.plot(ax=ax1, color=gdf['lgc00_15cl3'].map(colors), legend=True)
# centers.plot(ax=ax, column='capital', marker='*', markersize=1, color='black')
# plt.axis('off')
ax1.set_xticks([])
ax1.set_yticks([])
ax1.set_title("Mapa de Rezago Social a nivel municipal, 2015.", **csfont)
txt = "Categorías de Rezago Social sugeridas por Valdez-Cruz y Vargas-Chanes (2017)."
ax1.text(0.01, 0.01, txt, wrap=True, horizontalalignment='left', fontsize=12, **csfont)
ax1.legend(handles=legend_elements)
###
gdf.plot(ax=ax2, color=gdf['lgc00_15cl3'].map(colors), legend=True)
# centers.plot(ax=ax, column='capital', marker='*', markersize=1, color='black')
# plt.axis('off')
ax2.set_xticks([])
ax2.set_yticks([])
ax2.set_title("Mapa de Rezago Social a nivel municipal, 2015.", **csfont)
txt = "Categorías de Rezago Social sugeridas por Valdez-Cruz y Vargas-Chanes (2017)."
ax2.text(0.01, 0.01, txt, wrap=True, horizontalalignment='left', fontsize=12, **csfont)
ax2.legend(handles=legend_elements)
###
plt.show()
