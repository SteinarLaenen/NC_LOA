import numpy as np
import matplotlib.pyplot as plt    

##initialization
f_g = np.Inf
m = 30
n = 20000
alpha1 = 3
alpha2 = 1
omega = 0.7
lower_limit = -100
upper_limit = 100
iterations = 1000

def HC(x):
    sum = 0.0
    for i in range(1, len(x) + 1):
        sum += ((10 ** 6) ** ((i - 1) / (len(x) - 1))) * x[i - 1] ** 2
    return sum

o = np.random.uniform(-80, 80, (1, m))

def SHC(x):
    F_1 = 100
    return HC((x - o).T) + F_1



x = lower_limit + (upper_limit - lower_limit)*np.random.uniform(0, 1, (n, m))
v = np.zeros(x.shape)
f_p = SHC(x)
print(f_p.shape)

p = x
g = x[np.argmin(f_p)]

track = []

for i in range(iterations):
    f_i = SHC(x)
    
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
    

print(g)
print(o)
    
plt.plot(np.arange(iterations), track)
plt.show()








## Steinar implements the PSO algorithm
## Liam does the LOA algorithm
