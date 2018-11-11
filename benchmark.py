# Lion Optimisation Algorithm implementation
# Natural computing assignment
# Python3.6.6
# Benchmark functions for testing of LOA and PSO

import numpy as np
from matplotlib import pyplot as plt

def Discus(x):
    sum = 0.0
    for i in range(2, len(x)+1):
        sum += x[i-1] ** 2
    sum += (10**6) * (x[i-1] ** 2)
    return sum

def RDiscus(x, o):
    F_3 = 300
    return Discus((x - o).T) + F_3
    
def BC(x):
    sum = 0.0
    sum += x[1] ** 2
    for i in range(2, len(x) + 1):
        sum += (x[i - 1] ** 2)
    sum *= (10**6)
    return sum

def RBC(x, o):
    F_2 = 200
    return BC((x - o).T) + F_2
    
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
    return Katsuura(5*(x - o)/100) + 1200
