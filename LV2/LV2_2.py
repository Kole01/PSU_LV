## drugi

import numpy as np
import matplotlib.pyplot as plt

a= []
for x in range (100):
    a.append(np.random.randint(1,7))
    print(a)

x = np.linspace(0,7,num=100)
plt.hist(a,bins= 50,)
plt.show()














