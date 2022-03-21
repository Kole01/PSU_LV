import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10, num = 20)
y = np.linspace(0,10, num = 20)
x = np.array([1,2,3,3,1])
y = np.array([1,2,2,1,1])

plt.axis([0,4,0,4])
plt.plot(x,y,'b.-')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('zdtk 1')
plt.show()