import numpy as np
import random


def generateGroups(nPop, sexRate, prideNo, percentNomad):

    # init array of prideNo pride groups
    #prideArray = np.array([Group(True) for i in range(prideNo)])

    # expected number of lions in each structure
    nomadPop = int(round(nPop * percentNomad, 0))
    pridePop = nPop - nomadPop

    # init array of nomad lions
    nomadLionsArray = np.array([Lion() for i in range(nomadPop)])

    # init array of pride lions
    prideLionsArray = np.array([Lion() for i in range(pridePop)])


    # bit array to determine whether lion is a male
    # eg. [0,1,0,0,0,1] indicates the second and last lion to be males
    # the rest being females
    malePrideIndicies = np.zeros(pridePop)
    maleNomadIndicies = np.zeros(nomadPop)

    # the number of expected males in the population of prides and nomads
    noPrideMales = int(round(nomadPop * (1 - sexRate), 0))
    noNomadMales = int(round(nomadPop * (sexRate), 0))

    # generate bit array with correct no of males
    for i in range(noMales):
        maleIndicies[i] = 1

    # mix up the distribution of males a bit
    random.shuffle(maleIndicies)


    #while




# represents a pride or a nomad group
class Group:

    def __init__(self, isPride):

        self.isPride = isPride
        self.lionArray = None




class Lion:

    def __init__(self):

        self.isMale = None
        self.bestVisitedPosition = None
        self.groupID = None             # id of the pride or nomad of the Lion
        self.strength = None
        self.isMature = None
