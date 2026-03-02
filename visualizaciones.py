import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos
df = pd.read_csv("data/WB_WDI_SP_DYN_LE00_IN.csv")
df["OBS_VALUE"] = pd.to_numeric(df["OBS_VALUE"], errors="coerce")
df = df[["REF_AREA_LABEL", "TIME_PERIOD", "OBS_VALUE"]].dropna()

sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle("Life Expectancy Analysis — World Bank Data", fontsize=15, fontweight="bold")

# 1. Evolución Argentina vs países vecinos
paises = ["Argentina", "Brazil", "Chile", "Uruguay", "Bolivia"]
for pais in paises:
    datos = df[df["REF_AREA_LABEL"] == pais].sort_values("TIME_PERIOD")
    if not datos.empty:
        axes[0,0].plot(datos["TIME_PERIOD"], datos["OBS_VALUE"], marker="o", markersize=3, label=pais)
axes[0,0].set_title("Life Expectancy — Argentina vs Neighbors")
axes[0,0].set_xlabel("Year")
axes[0,0].set_ylabel("Years")
axes[0,0].legend(fontsize=8)

# 2. Top 10 países con mayor esperanza de vida promedio
promedios = df.groupby("REF_AREA_LABEL")["OBS_VALUE"].mean().sort_values(ascending=False).head(10)
axes[0,1].barh(promedios.index[::-1], promedios.values[::-1], color=sns.color_palette("Greens_r", 10))
axes[0,1].set_title("Top 10 Countries by Average Life Expectancy")
axes[0,1].set_xlabel("Average Years")

# 3. Países con menor esperanza de vida promedio
menores = df.groupby("REF_AREA_LABEL")["OBS_VALUE"].mean().sort_values().head(10)
axes[1,0].barh(menores.index[::-1], menores.values[::-1], color=sns.color_palette("Reds_r", 10))
axes[1,0].set_title("Bottom 10 Countries by Average Life Expectancy")
axes[1,0].set_xlabel("Average Years")

# 4. Evolución global promedio por año
global_avg = df.groupby("TIME_PERIOD")["OBS_VALUE"].mean()
axes[1,1].plot(global_avg.index, global_avg.values, color="#2E86AB", linewidth=2, marker="o", markersize=3)
axes[1,1].fill_between(global_avg.index, global_avg.values, alpha=0.2, color="#2E86AB")
axes[1,1].set_title("Global Average Life Expectancy Over Time")
axes[1,1].set_xlabel("Year")
axes[1,1].set_ylabel("Years")

plt.tight_layout()
plt.savefig("life_expectancy_analysis.png", dpi=150, bbox_inches="tight")
plt.show()
print("Guardado: life_expectancy_analysis.png")