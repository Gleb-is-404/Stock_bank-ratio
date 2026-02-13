import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_Quality = pd.read_excel("Quality.xlsx")

df_Bank = pd.read_excel("Bank.xlsx")
df_Stock = pd.read_excel("Stock.xlsx")
df_merged = pd.merge(df_Stock, df_Bank, on="Country")
df_merged["Ratio"] = df_merged["Stock market"] / df_merged["Bank credit"]
df_final=df_merged.merge(df_Quality, on="Country", how="inner")
df_final=df_final[df_final["Ratio"]<2.5]
plt.figure(figsize=(8,6))
plt.scatter(df_final["Ratio"], df_final["Quality"])
for x, y, label in zip(df_final["Ratio"], df_final["Quality"], df_final["Country"]):
    plt.annotate(
        label,
        (x, y),
        textcoords="offset points",
        xytext=(5, 5),
        ha="left"
    )
plt.xlabel("Stock market to Bank credit ration")
plt.ylabel("Quality")
plt.title("Stock-to-Bank Ratio vs Quality by Country")
plt.grid(True)
plt.legend()

x = df_final["Ratio"]
y = df_final["Quality"]


slope, intercept = np.polyfit(x, y, 1) 
y_trend = slope * x + intercept
plt.text(
    x.min()+0.45, y.max()-14, 
    f"y = {slope:.2f}x + {intercept:.2f}", 
    fontsize=10, 
    verticalalignment='top',
    color='red',
    rotation=-7.5
)
plt.plot(x, y_trend, color='red', linewidth=2, label='Trend line')
plt.show()

