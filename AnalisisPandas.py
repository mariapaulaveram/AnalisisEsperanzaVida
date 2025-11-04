import pandas as pd


# Cargar el archivo
df = pd.read_csv("C:/Users/trezz/Desktop/proyectosDeDesarrolloWeb/AnalisisEsperanzaVida/data/WB_WDI_SP_DYN_LE00_IN.csv")

# Convertir valores a numéricos (por si hay texto o nulos)
df["OBS_VALUE"] = pd.to_numeric(df["OBS_VALUE"], errors="coerce")

# Filtrar columnas útiles, elimina todas las filas que tengan al menos un valor nulo (NaN) en esas columnas
print("\n *Filtra columnas útiles:")
df = df[["REF_AREA_LABEL", "TIME_PERIOD", "OBS_VALUE"]].dropna()
print(df.head())

#Calcular estadísticas por país
estadisticas_paises = df.groupby("REF_AREA_LABEL")["OBS_VALUE"].agg(
    mean="mean",
    median="median",
    std="std",
    min="min",
    max="max",
    count="count"
).round(2)

#Ordena los países de mayor a menor según su esperanza de vida promedio
print("\n *Estadísticas por país segun su esperanza de vida promedio:")
print(estadisticas_paises.sort_values("mean", ascending=False).head(10))  # Top 10 por media

#Ese bloque de código está diseñado para identificar el país cuya esperanza de vida ha variado más a lo largo del tiempo
#Identificar el país más variable
pais_mas_variable = estadisticas_paises["std"].idxmax()
valor_std_max = estadisticas_paises["std"].max()
print(f"\n *País con mayor variabilidad en esperanza de vida: {pais_mas_variable} ({valor_std_max:.2f} años)")
print("\n *Estadísticas del país más variable:")
print(estadisticas_paises.loc[pais_mas_variable])




