import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

mtcars = pd.read_csv('mtcars.csv') 

#print("Najvecu potrosnju imaju:")
#print(mtcars.sort_values(by=['mpg']).head(5).car)

#print("Najmanju potrosnju s 8 cilindara imaju: ")
#print(mtcars[(mtcars.cyl==8)].sort_values(by=['mpg'], ascending=False).head(3))

#print("Srednja vrijednost potrosnje s 6 cilindara: ")
#print(mtcars[(mtcars.cyl==6)].mpg.mean())

#print("Srednja vrijednost potrosnje s 4 cilindra: ")
#print(mtcars[(mtcars.cyl==4) & (mtcars.wt>2.0) & (mtcars.wt<2.2)].mpg.mean())

#print("Auti s rucnim i automatskim mjenjacem: ")
#print(mtcars.value_counts('am'))

#print("Automobili s automatskim mjenjacem i vise od 100hp")
#print(len(mtcars[(mtcars.am==1)&(mtcars.hp>100)]))

mtcars['kg']=mtcars['wt']*1000*0.453
print("Automobili u kilogramima")
print(mtcars['car','kg'])