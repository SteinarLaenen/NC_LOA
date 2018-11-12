import numpy as np
import matplotlib.pyplot as plt    
from benchmark import *

def main():
    # adjustable parameters
    m = 30
    n = 50
    alpha1 = 2
    alpha2 = 2
    omega = 0.7
    lower_limit = -100
    upper_limit = 100
    iterations = 3000
    runs = 60
    o = np.random.uniform(-80, 80, (1, m))

    # initialize matrix that saves all values
    # each row is one run of the algorithm, containing the progress of global best per iterations
    # each column is the value at each iteration for all the runs
    training_curves = np.zeros((runs, iterations))

    for run in range(runs):
        # set each row to be one run of the algorithm
        training_curves[run] = PSO(m, n, alpha1, alpha2,
                                   omega, lower_limit, upper_limit,
                                   iterations, SHC, o)


        if run % 10 == 0:
            print("number of runs completed = ", run,  "/", runs)

    # get average and std of all iterations
    average_train_curve = np.mean(training_curves, axis = 0)
    standard_dev_train_curve = np.std(training_curves, axis = 0)

    # find max/min/mean/std value of the best found (last element)
    maximum = np.max(training_curves[:, -1])
    minimum = np.min(training_curves[:, -1])
    mean = average_train_curve[-1]
    std = standard_dev_train_curve[-1]

    # print results
    print('maximum: {:.2e}'.format(maximum))
    print('minimum: {:.2e}'.format(minimum))
    print('mean: {:.2e}'.format(mean))
    print('std: {:.2e}'.format(std))

    # plot
    plt.plot(np.arange(iterations), average_train_curve)
    plt.title('global found minimum per iteration')
    plt.xlabel('iterations')
    plt.ylabel('global_best (all time)')
    plt.yscale('log')
    plt.show()

    

def PSO(m, n, alpha1, alpha2, omega, lower_limit, upper_limit, iterations, fitness, o):
    """
    implementation of PSO algorithm.
    """

    ##initialize particles. Each row is one particle.
    f_g = np.Inf
    x = np.random.uniform(lower_limit, upper_limit, (n, m))
    v = np.zeros(x.shape)
    f_p = fitness(x, o)

    # p vector is the personal best vector
    p = x
    # g vector is a single vectot that is the global best
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
        v = omega*v + alpha1*np.random.uniform(0, 1, (n, m))*(p - x) + \
            alpha2*np.random.uniform(0, 1, (n, m))*(g - x)

        # update positions  
        x = x + v
    
        track.append([f_g])

    return np.resize(np.array(track), (3000,))

if __name__ == "__main__":
    main()
