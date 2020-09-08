import os
import pandas as pd
import sqlite3

FOLDER = 'denue'
COL_NAMES = ["id", "nom_estab", "raz_social", "codigo_act", "nombre_act", "per_ocu", "tipo_vial", "nom_vial",
             "tipo_v_e_1", "nom_v_e_1", "tipo_v_e_2", "nom_v_e_2", "tipo_v_e_3", "nom_v_e_3", "numero_ext", "letra_ext",
             "edificio", "edificio_e", "numero_int", "letra_int", "tipo_asent", "nomb_asent", "tipoCenCom",
             "nom_CenCom", "num_local", "cod_postal", "cve_ent", "entidad", "cve_mun", "municipio", "cve_loc",
             "localidad", "ageb", "manzana", "telefono", "correoelec", "www", "tipoUniEco", "latitud", "longitud",
             "fecha_alta"]

df = pd.DataFrame()
for file in os.listdir(FOLDER):
    file = os.path.join(FOLDER, file)
    if os.path.isfile(file) and 'csv' in file:
        for encoding in ('utf8', 'cp1258'):
            print(file, encoding)
            try:
                temp = pd.read_csv(file, encoding=encoding, low_memory=False)
            except UnicodeDecodeError as e:
                print(f"\nDecodeError: {file}\n")
            else:
                break
        temp.columns = COL_NAMES
        df = pd.concat([temp, df], axis=0, ignore_index=True)
        print(df.shape, temp.shape)

df.to_csv("denue.csv")
conn = sqlite3.connect('denue.sqlite3')
df.to_sql('denue', conn, if_exists='replace', index=False)
