import numpy as np
import matplotlib.pyplot as plt

def HC(x):
    sum = 0.0
    for i in range(1, len(x) + 1):
        sum += ((10 ** 6) ** ((i - 1) / (len(x) - 1))) * x[i - 1] ** 2
    return sum

##initialization
f_g = np.Inf
m = 100
n = 100000
alpha1 = 1
alpha2 = 3
omega = 0.7
# lower_limit = 0
# upper_limit = 1
iterations = 100

x = np.random.uniform(0, 1, (n, m))
v = np.zeros(x.shape)
f_p = HC(x.T)

p = x
g = x[np.argmin(f_p)]

track = []

for i in range(iterations):
    f_i = HC(x.T)
    
    cond = f_i < f_p
    p[cond] = x[cond]
    f_p[cond] = f_i[cond]

    ## update global best (all time)
    if np.min(f_p) < f_g:
        f_g = np.min(f_p)
        g = g = x[np.argmin(f_p)]

    v = omega*v + alpha1*np.random.uniform(0, 1, (n, 1))*(p - x) + \
        alpha2*np.random.uniform(0, 1, (n, 1))*(g - x)

    x = x + v
    
    track.append([f_g])
    

plt.plot(np.arange(iterations), track)
plt.show()








## Steinar implements the PSO algorithm
## Liam does the LOA algorithm
