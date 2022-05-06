import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ucitavanje ociscenih podataka
df = pd.read_csv('cars_processed.csv')
print(df.info())


print("Najmanju cijenu ima: ", df.sort_values(by=["selling_price"]).head(1))
print("Najvecu cijenu ima: ", df.sort_values(by=["selling_price"]).tail(1))

print("Iz 2012 ima: ",sum(df["year"]==2012))

print("Najmanje kilometara ima: ", df.sort_values(by=["km_driven"]).head(1))
print("Najvise kilometara ima: ", df.sort_values(by=["km_driven"]).tail(1))

print("Sjedala: ", sum(df["seats"]))

