import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
def returns_dydt(y,t):
	dydt=13*np.exp(t)+y
	return dydt
yo=1
t=np.linspace(0,5)
y=odeint(returns_dydt,yo,t)
plt.plot(t,y)
plt.xlabel("TIME")
plt.ylabel("Y")
plt.show()
