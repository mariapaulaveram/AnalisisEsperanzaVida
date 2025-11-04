import pandas as pd

# Cargar el archivo
df = pd.read_csv("C:/Users/trezz/Desktop/proyectosDeDesarrolloWeb/PandasProject/data/WB_WDI_SP_DYN_LE00_IN.csv")

#Exploracion Inicial
print("\n *Forma del DataFrame (filas, columnas):")
print(df.shape)
print("\n *Primeras filas del dataset:")
print(df.head())
print("\n *Información general del DataFrame:")
print(df.info())
print("\n *Cantidad de valores nulos por columna:")
print(df.isnull().sum())
print("\n")

# Convertir valores a numéricos (por si hay texto o nulos)
df["OBS_VALUE"] = pd.to_numeric(df["OBS_VALUE"], errors="coerce")

# Filtrar columnas útiles, elimina todas las filas que tengan al menos un valor nulo (NaN) en esas columnas
print("\n *Filtra columnas útiles:")
df = df[["REF_AREA_LABEL", "TIME_PERIOD", "OBS_VALUE"]].dropna()
print(df.head())

# Filtrar por país
print("\n *Filtra Argentina:")
arg = df[df["REF_AREA_LABEL"] == "Argentina"]
print(arg[["TIME_PERIOD", "OBS_VALUE"]].sort_values("TIME_PERIOD"))

# Promedios por país
print("\n *Promedios por país:")
promedios = df.groupby("REF_AREA_LABEL")["OBS_VALUE"].mean().sort_values(ascending=False)
print(promedios)

#Pivotar la tabla
print("\n *Tabla pivotada:")
tabla_pivot = df.pivot_table(
    index="REF_AREA_LABEL",
    columns="TIME_PERIOD",
    values="OBS_VALUE",
    aggfunc="mean"
)
tabla_pivot = tabla_pivot.round(2)
print(tabla_pivot.head())
print("\n")

#Agrupar por país y año
agrupado = df.groupby(["REF_AREA_LABEL", "TIME_PERIOD"])["OBS_VALUE"].mean().reset_index()
print("\n *Agrupado por pais y por año:")
print(agrupado)
print("\n")

#Comparar países en un año específico (ej. 2020)
print("\n *Países con mayor esperanza de vida en 2020:")
comparacion_2020_mayor = tabla_pivot[2020].sort_values(ascending=False)
print(comparacion_2020_mayor.head(10))  # Top 10 países

print("\n *Países con menor esperanza de vida en 2020:")
comparacion_2020_menor = tabla_pivot[2020].sort_values()
print(comparacion_2020_menor.head(10))  # Top -10 países
print("\n")

#Comparar países en un año específico (ej. 1988)
print("\n *Países con mayor esperanza de vida en 1988:")
comparacion_1988_mayor = tabla_pivot[1988].sort_values(ascending=False)
print(comparacion_1988_mayor.head(10))  # Top 10 países

print("\n *Países con menor esperanza de vida en 1988:")
comparacion_1988_menor = tabla_pivot[1988].sort_values()
print(comparacion_1988_menor.head(10))  # Top -10 países
print("\n")


#Valores extremos de esperanza de vida en toda la tabla
valor_max = tabla_pivot.max().max()
valor_min = tabla_pivot.min().min()

# Ubicar el país y año del valor máximo
pais_max = tabla_pivot[tabla_pivot == valor_max].stack().index[0][0]
anio_max = tabla_pivot[tabla_pivot == valor_max].stack().index[0][1]

# Ubicar el país y año del valor mínimo
pais_min = tabla_pivot[tabla_pivot == valor_min].stack().index[0][0]
anio_min = tabla_pivot[tabla_pivot == valor_min].stack().index[0][1]

print(f"Mayor esperanza de vida: {valor_max:.2f} años en {pais_max} ({anio_max})")
print(f"Menor esperanza de vida: {valor_min:.2f} años en {pais_min} ({anio_min})")
