import numpy as np
import matplotlib.pyplot as plt

time = np.arange(0,2*np.pi,0.1)
sin = np.sin(time)
cos = np.cos(time)
plt.plot(time, sin, time, cos)
plt.axhline(y=0, color = 'black')
plt.show()
