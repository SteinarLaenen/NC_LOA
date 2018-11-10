# Lion Optimisation Algorithm implementation
# Natural computing assignment
# Python3.6.6
# Main LOA engine

# library imports
import LOA_lib
import benchmark
import sys, time
import numpy as np
import matplotlib.pyplot as plt


# set algorithm params as global variables
prideNo = 4             # number of pride structures
percentNomad = 0.2      # portion of population to be nomads
roamingPercent = 0.2
mutateProb = 0.2
sexRate = 0.8
mateProb = 0.3
migrateRate = 0.4
nPop = 50
upper_limit = -100
lower_limit = 100
dim = 30
evaluation = benchmark.SHC
o = np.random.uniform(-80, 80, (1, dim))
maxIterationNo = 5000


''' steps 1 & 2 '''
# initialise the populations into structures of prides and nomads
prideArray, nomadLionsArray = LOA_lib.generateGroups(nPop, sexRate, prideNo, percentNomad,
                                                     upper_limit, lower_limit, dim, evaluation, o)

global_best = [np.inf]
for it in range(maxIterationNo):
    start_time = time.time()
    # update the list of best scores obtained for each iteration
    prideArray, nomadLionsArray = LOA_lib.updateBestScoreList(prideArray, nomadLionsArray)


    ''' step 3 '''
    prideArray = LOA_lib.hunting(prideArray)
    prideArray = LOA_lib.moveToSafePlace(prideArray)
    prideArray = LOA_lib.pridesRoam(prideArray, roamingPercent)
    prideArray = LOA_lib.prideMating(prideArray, mateProb,
                                     mutateProb, lower_limit, upper_limit, o)
    prideArray, nomadLionsArray = LOA_lib.prideDefense(prideArray, nomadLionsArray,
                                                       sexRate, nPop, percentNomad, prideNo)


    ''' step 4 '''
    # move nomads about randomly in search space
    nomadLionsArray = LOA_lib.nomadsRoam(nomadLionsArray, lower_limit, upper_limit, dim)

    # nomads mate
    nomadLionsArray = LOA_lib.mateNomads(nomadLionsArray, mateProb, mutateProb, lower_limit, upper_limit, o)

    # nomad male randomly attack pride
    prideArray, nomadLionsArray = LOA_lib.nomadsAttackPride(prideArray, nomadLionsArray)


    ''' step 5 '''
    # females migrate from a pride and join the nomads with some probability
    prideArray, nomadLionsArray = LOA_lib.migrateFemaleFromPride(prideArray, nomadLionsArray, migrateRate, sexRate)


    ''' step 6 '''
    # allocate some female nomad lions to the prides
    # kill off the least fit nomad lions
    prideArray, nomadLionsArray = LOA_lib.step6(prideArray, nomadLionsArray, nPop, sexRate, percentNomad, prideNo)

    '''best score obtained so far'''
    current_best = LOA_lib.getCurrentGlobalBest(prideArray, nomadLionsArray)
    if current_best < global_best[-1]:
        global_best.append([current_best])
        print("improved score: %.2E" % current_best)
    else:
        global_best.append(global_best[-1])

    elapsed_time = (time.time() - start_time)

    

