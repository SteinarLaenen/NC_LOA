# Lion Optimisation Algorithm implementation
# Natural computing assignment
# Python3.6.6
# Benchmark functions for testing of LOA and PSO

import numpy as np
from matplotlib import pyplot as plt


def HC(x):
    sum = 0.0
    for i in range(1, len(x) + 1):
        sum += ((10 ** 6) ** ((i - 1) / (len(x) - 1))) * x[i - 1] ** 2
    return sum


def SHC(x, o):
    F_1 = 100
    return HC((x - o).T) + F_1


def Katsuura(x):
    x = x.T
    sum = 0.0
    product = 1.0
    for i in range(len(x)):
        summation = 0
        for j in range(1, 32):
            term = 2 ** j * x[i]
            summation += np.absolute(term - np.round(term)) / (2 ** j)
        #product *= np.pow(1 + ((i + 1) * summation), 10 / np.pow(len(x), 1.2))
        product *= (1 + ((i + 1) * summation) ** (10 / (len(x) ** 1.2)))
    sum = (10.0 / len(x) * len(x)) * product - (10.0 / len(x) * len(x))
    return sum

def SRKatsuura(x, o):
    Katsuura(5*(x - o)/100) + 1200
