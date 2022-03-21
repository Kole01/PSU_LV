import numpy as np
import matplotlib.pyplot as plt

data   =   np.loadtxt(open("mtcars.csv",   "rb"),   usecols=(1,2,3,4,5,6), delimiter=",", skiprows=1)

plt.scatter(data[:,0],data[:,3], c='b',s=data[:,2])
mpg = data[:,0]
hp=data[:,3]
plt.scatter(mpg,hp)
plt.xlabel('mpg')
plt.ylabel('hp')
plt.show()

print(data)













