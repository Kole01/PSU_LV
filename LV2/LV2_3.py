from turtle import width
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(open("mtcars.csv","rb"),usecols=(1,2,3,4,5,6), delimiter=",",skiprows=1)

mpg = data[:,0]
hp = data[:,3]
wt = data[:,5]
cyl = data[:,1]
array = []

print ("Minimalna potrosnja : ", max(mpg))
print ("Maksimalna potorsnja potrosnja : ", min(mpg))
print ("Srednja vrijednost: ", np.mean(mpg))

for i in range(32):
    if cyl[i]==6:
        array.append(data[i:0])

print ("Minimalna potrosnja 6 : ", max(array))
print ("Maksimalna potorsnja potrosnja  6: ", min(array))
print ("Srednja vrijednost: 6 ", np.mean(array))

plt.scatter(mpg,hp,s=width*80)
plt.xlabel("mph")
plt.ylabel("hp")
plt.show()