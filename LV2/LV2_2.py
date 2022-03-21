from asyncio.windows_events import NULL
import numpy as np
import matplotlib.pyplot as plt

dob_broj=[]
for i in range(0,100):
    dob_broj.append(np.random.randint(1,7))
    
print(dob_broj)
x = np.linspace(0,7,num=100)
plt.hist(dob_broj,bins= 50,)
plt.show()