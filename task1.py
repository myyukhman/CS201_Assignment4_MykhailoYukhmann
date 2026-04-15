import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("random_walk.csv")

df["distance"] = (df["x"] **2 + df["y"] ** 2)**(1/2)

max = df["distance"].max()
avrg = df["distance"].mean()

