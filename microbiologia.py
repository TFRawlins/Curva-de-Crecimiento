import pandas as pd
import math
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Tiempo [h]": [0,     2,   4,   6,   8,  10, 12, 14, 16, 18, 20, 22, 24, 26, 28],
    "OD 600 nm":  [0.1, 0.1, 0.1, 0.1, 0.3, 0.9, 0.5, 0.9, 0.8, 0.9, 0.5, 0.4, 0.5, 0.4, 0.2],
    "FD":         [1,     1,   1,   1,   1,   1, 4, 4, 10, 10, 20, 20, 20, 20, 20],
    "X UFC/mL":   [],
    "Ln (X/Xo)":  []
}



for i in range(len(data["OD 600 nm"])):
    y = data["OD 600 nm"][i]
    FD = data["FD"][i]
    x = (1000*y + 3.2)
    data["X UFC/mL"].append(x*FD)

Xo = data["X UFC/mL"][0] 
for X in data["X UFC/mL"]:
    ln_X_Xo = math.log(X / Xo)
    data["Ln (X/Xo)"].append(ln_X_Xo)


for l in data:
    print(data[l])

df = pd.DataFrame(data)

sns.set(style="whitegrid")
sns.set_palette("pastel")

plt.figure(figsize=(10, 6))
sns.lineplot(x="Tiempo [h]", y="Ln (X/Xo)", data=df, marker='o', linestyle='-', color='teal', markersize=8, lw=2)
plt.xticks(ticks=df["Tiempo [h]"], fontsize=12)
plt.title('Curva de Crecimiento Logarítmica', fontsize=16)
plt.xlabel('Tiempo [h]', fontsize=14)
plt.ylabel('Ln (X/Xo)', fontsize=14)
plt.grid(False) 
plt.show()