# código de geração do gráfico
import pandas as pd
import matplotlib.pyplot as plt

# Read the data from gasolina.csv
data = pd.read_csv("gasolina.csv")

# Create a line chart
plt.figure(figsize=(10, 6))
plt.plot(data["dia"], data["venda"], marker='o', color='b')
plt.xlabel("Dia")
plt.ylabel("Valor")
plt.title("Valor médio da Gasolina por Dia")
plt.grid(True)

# Save the chart as gasolina.png
plt.savefig("gasolina.png")
