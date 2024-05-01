import numpy as np
from matplotlib import pyplot as plt
t=np.arange(0,1,0.001)
f1=5
f2=10
x1=np.sin(2*np.pi*f1*t)
x2=np.sin(2*np.pi*f2*t)
sub=(x2+x1)
plt.plot(t,sub)
plt.xlabel("time")
plt.ylabel("amplitude")
plt.title("sinewave")
plt.show()
