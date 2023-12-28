import numpy as np
import pandas as pd

df = pd.read_csv("credit.csv", delimiter=" ")

print(df)

print(df[["Age", "Education"]])