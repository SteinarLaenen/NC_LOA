import numpy as np
import matplotlib.pyplot as plt
import matplotlib


'''--------------------- RBC -------------------------------'''
font = {'family' : 'normal',
        'size'   : 13}

matplotlib.rc('font', **font)

rbcCurrentBestCurve = np.load("./LOA/RBC/globalBestCurves.npy")
rbcAverageCurrentBest = np.median(rbcCurrentBestCurve, axis = 0)
rbcStdCurrentBest = np.std(rbcCurrentBestCurve, axis = 0)

maximum = np.max(rbcCurrentBestCurve[:, -1])
minimum = np.min(rbcCurrentBestCurve[:, -1])
median = rbcAverageCurrentBest[-1]
std = rbcStdCurrentBest[-1]

# print results
print("RBC")
print('maximum: {:.2e}'.format(maximum))
print('minimum: {:.2e}'.format(minimum))
print('median: {:.2e}'.format(median))
print('std: {:.2e}'.format(std))

# plot
plt.plot(np.arange(len(rbcAverageCurrentBest)), rbcAverageCurrentBest, label = "LOA")
plt.title('global found minimum per iteration')
plt.xlabel('iterations')
plt.ylabel('global_best (all time)')
plt.yscale('log')

plt.show()




'''--------------------- SHC -------------------------------'''
rbcCurrentBestCurve = np.load("./LOA/SHC/globalBestCurves.npy")
rbcAverageCurrentBest = np.median(rbcCurrentBestCurve, axis = 0)
rbcStdCurrentBest = np.std(rbcCurrentBestCurve, axis = 0)

maximum = np.max(rbcCurrentBestCurve[:, -1])
minimum = np.min(rbcCurrentBestCurve[:, -1])
median = rbcAverageCurrentBest[-1]
std = rbcStdCurrentBest[-1]

# print results
print("SHC")
print('maximum: {:.2e}'.format(maximum))
print('minimum: {:.2e}'.format(minimum))
print('median: {:.2e}'.format(median))
print('std: {:.2e}'.format(std))

# plot
plt.plot(np.arange(len(rbcAverageCurrentBest)), rbcAverageCurrentBest, label = "LOA")
plt.title('Global Found Minimum per Iteration (Log) (SHC)')
plt.xlabel('Iterations')
plt.ylabel('Global_Best (all time)')
plt.yscale('log')

'''PSO--------------------- SHC -------------------------------'''
rbcCurrentBestCurve = np.load("./PSO/SHC/PSO_SHC_trainingcurves.npy")
rbcAverageCurrentBest = np.median(rbcCurrentBestCurve, axis = 0)
rbcStdCurrentBest = np.std(rbcCurrentBestCurve, axis = 0)

maximum = np.max(rbcCurrentBestCurve[:, -1])
minimum = np.min(rbcCurrentBestCurve[:, -1])
median = rbcAverageCurrentBest[-1]
std = rbcStdCurrentBest[-1]

# print results
print("SHC")
print('maximum: {:.2e}'.format(maximum))
print('minimum: {:.2e}'.format(minimum))
print('median: {:.2e}'.format(median))
print('std: {:.2e}'.format(std))

# plot
plt.plot(np.arange(len(rbcAverageCurrentBest)), rbcAverageCurrentBest, label = "PSO")
plt.yscale('log')
plt.legend()

plt.show()



'''--------------------- RDiscus -------------------------------'''
rbcCurrentBestCurve = np.load("./LOA/RDiscus/globalBestCurves.npy")
rbcAverageCurrentBest = np.median(rbcCurrentBestCurve, axis = 0)
rbcStdCurrentBest = np.std(rbcCurrentBestCurve, axis = 0)

maximum = np.max(rbcCurrentBestCurve[:, -1])
minimum = np.min(rbcCurrentBestCurve[:, -1])
median = rbcAverageCurrentBest[-1]
std = rbcStdCurrentBest[-1]

# print results
print("RDiscus")
print('maximum: {:.2e}'.format(maximum))
print('minimum: {:.2e}'.format(minimum))
print('median: {:.2e}'.format(median))
print('std: {:.2e}'.format(std))

# plot
plt.plot(np.arange(len(rbcAverageCurrentBest)), rbcAverageCurrentBest)
plt.title('global found minimum per iteration')
plt.xlabel('iterations')
plt.ylabel('global_best (all time)')
plt.yscale('log')

plt.show()

'''--------------------- RRosenbrock -------------------------------'''
rbcCurrentBestCurve = np.load("./LOA/SRosenbrock/globalBestCurves.npy")
rbcAverageCurrentBest = np.median(rbcCurrentBestCurve, axis = 0)
rbcStdCurrentBest = np.std(rbcCurrentBestCurve, axis = 0)

maximum = np.max(rbcCurrentBestCurve[:, -1])
minimum = np.min(rbcCurrentBestCurve[:, -1])
median = rbcAverageCurrentBest[-1]
std = rbcStdCurrentBest[-1]

# print results
print("SRosenbrock")
print('maximum: {:.2e}'.format(maximum))
print('minimum: {:.2e}'.format(minimum))
print('median: {:.2e}'.format(median))
print('std: {:.2e}'.format(std))

# plot
plt.plot(np.arange(len(rbcAverageCurrentBest)), rbcAverageCurrentBest)
plt.title('global found minimum per iteration')
plt.xlabel('iterations')
plt.ylabel('global_best (all time)')
plt.yscale('log')

plt.show()

'''--------------------- SRastrigin -------------------------------'''
rbcCurrentBestCurve = np.load("./LOA/SRastrigin/globalBestCurves.npy")
rbcAverageCurrentBest = np.median(rbcCurrentBestCurve, axis = 0)
rbcStdCurrentBest = np.std(rbcCurrentBestCurve, axis = 0)

maximum = np.max(rbcCurrentBestCurve[:, -1])
minimum = np.min(rbcCurrentBestCurve[:, -1])
median = rbcAverageCurrentBest[-1]
std = rbcStdCurrentBest[-1]

# print results
print("SRastrigin")
print('maximum: {:.2e}'.format(maximum))
print('minimum: {:.2e}'.format(minimum))
print('median: {:.2e}'.format(median))
print('std: {:.2e}'.format(std))

# plot
plt.plot(np.arange(len(rbcAverageCurrentBest)), rbcAverageCurrentBest, label = "LOA")
plt.title('Global Found Minimum per Iteration (Log) (Rastrigin)')
plt.xlabel('Iterations')
plt.ylabel('Global_best (all time)')
plt.yscale('Log')

rbcCurrentBestCurve = np.load("./PSO/SRastrigin/PSO_SRastrigin_trainingcurves.npy")
rbcAverageCurrentBest = np.median(rbcCurrentBestCurve, axis = 0)
rbcStdCurrentBest = np.std(rbcCurrentBestCurve, axis = 0)

maximum = np.max(rbcCurrentBestCurve[:, -1])
minimum = np.min(rbcCurrentBestCurve[:, -1])
median = rbcAverageCurrentBest[-1]
std = rbcStdCurrentBest[-1]

# print results
print("SRastrigin")
print('maximum: {:.2e}'.format(maximum))
print('minimum: {:.2e}'.format(minimum))
print('median: {:.2e}'.format(median))
print('std: {:.2e}'.format(std))

# plot
plt.plot(np.arange(len(rbcAverageCurrentBest)), rbcAverageCurrentBest, label = "PSO")
plt.legend()
plt.show()


