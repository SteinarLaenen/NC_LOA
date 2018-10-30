import numpy as np
import matplotlib.pyplot as plt    
from benchmark import *


def PSO(f_g, m, n, alpha1, alpha2, omega, lower_limit, upper_limit, iterations, fitness, o):
    """
    implementation of PSO algorithm.
    """

    ##initialize particles. Each row is one particle.
    x = lower_limit + (upper_limit - lower_limit)*np.random.uniform(0, 1, (n, m))
    v = np.zeros(x.shape)
    f_p = fitness(x, o)

    p = x
    g = x[np.argmin(f_p)]

    track = []

    for i in range(iterations):
        f_i = fitness(x, o)

        # Update personal bests
        cond = f_i < f_p
        p[cond] = x[cond]
        f_p[cond] = f_i[cond]

        # update global best (all time)
        if np.min(f_p) < f_g:
            f_g = np.min(f_p)
            g = g = x[np.argmin(f_p)]

        # compute velocity
        v = omega*v + alpha1*np.random.uniform(0, 1, (n, 1))*(p - x) + \
            alpha2*np.random.uniform(0, 1, (n, 1))*(g - x)

        # update positions  
        x = x + v
    
        track.append([f_g])
    
    plt.plot(np.arange(iterations), track)
    plt.show()
    print('{:.2e}'.format(f_g))

##initialization
f_g = np.Inf
m = 30
n = 50
alpha1 = 3
alpha2 = 1
omega = 0.7
lower_limit = -100
upper_limit = 100
iterations = 100
o = np.random.uniform(-80, 80, (1, m))
    
PSO(f_g, m, n, alpha1, alpha2, omega, lower_limit, upper_limit, iterations, SRKatsuura, o)








## Steinar implements the PSO algorithm
## Liam does the LOA algorithm
