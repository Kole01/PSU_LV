from tkinter.tix import COLUMN
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

mtcars = pd.read_csv('mtcars.csv') 

#mtcars.groupby('cyl')['mpg'].mean().plot(kind = 'bar')
#plt.show()

mtcars.boxplot(by='cyl', column='wt')
plt.show()