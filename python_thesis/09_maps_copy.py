import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from shapely.geometry import Point

gdf = gpd.read_file('municipios/areas_geoestadisticas_municipales.shp')
print(gdf.columns)
gdf['Key'] = gdf['CVE_ENT'] + gdf['CVE_MUN']
gdf['Area'] = gdf['geometry'].map(lambda p: p.area / 10**6)
gdf.drop(columns=['geometry']).to_csv('AREAS_Test.csv')
# rezago = pd.read_csv("rezago_social/rezago_social.csv")
# rezago_social = rezago[["lgc00_15cl3", "Key", "POB_TOTAL", "LAT", "LON"]]
# rezago_social['Key'] = rezago_social['Key'].astype(str).str.zfill(5)
#
# gdf = gdf.merge(rezago_social, on='Key')
#
# crs = gdf.crs
# geometry = [Point(xy) for xy in zip(gdf.LON, gdf.LAT)]
# centers = gpd.GeoDataFrame(crs={'init': 'epsg:4326'}, geometry=geometry)
# centers = centers.to_crs(crs)
# print(centers)
