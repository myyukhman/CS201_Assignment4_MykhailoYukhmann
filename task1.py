from cProfile import label

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("random_walk.csv")

df["distance"] = (df["x"] **2 + df["y"] ** 2)**(1/2)

max = df["distance"].max()
avrg = df["distance"].mean()

print(f"Max distance is {max}, average distance is {avrg}")

more_than_avrg = df[df["distance"] > avrg]
print(f"Filtered distance: {more_than_avrg}")

more_than_avrg.to_json("filtered_walk.json", orient="records")



plt.figure(figsize=(8, 4))
plt.plot(df["x"], df["y"], color="#430130", label="Walk trajectory")
plt.scatter(0,0, color="blue", marker="o", label="Start point")
last_x = df["x"].iloc[-1]
last_y = df["y"].iloc[-1]
plt.scatter(last_x, last_y, color="red", marker="x", label="Finish point")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Walk trajectory")


plt.show()