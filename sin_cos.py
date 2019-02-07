#ks indicates the changes that Ken Sherman made to the code
import numpy as np
import matplotlib.pyplot as plt

time = np.arange(0,2*np.pi,0.1)
sin = np.sin(time)
cos = np.cos(time)
tan = np.tan(time) #ks added tangent to the graph
plt.plot(time, sin, time, cos, time, tan)
plt.axhline(y=0, color = 'black')
axes = plt.gca()
axes.set_ylim([-1,1]) #ks setting y axis max and mins so we can see the plots
plt.show()
plt.savefig('hw2save.png') #ks this will save the plot locally
