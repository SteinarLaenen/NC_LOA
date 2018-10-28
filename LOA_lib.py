# Lion Optimisation Algorithm implementation
# Natural computing assignment
# Python3.6.6
# Auxiliary script for main LOA engine

# library imports
import numpy as np
import random


# initialises a population of lions based on the parameters specified
# and partitions them into the pride and nomad structures
def generateGroups(nPop, sexRate, prideNo, percentNomad, upper_limit, lower_limit, dim):

    # expected number of lions in each structure
    nomadPop = int(round(nPop * percentNomad, 0))
    pridePop = nPop - nomadPop

    ''' Initialize the positions of the Lions '''
    

    ''' setting up gender distribution for lions '''
    # bit array to determine whether lion is a male
    # eg. [0,1,0,0,0,1] indicates the second and last lion to be males
    # the rest being females
    malePrideIndicies = np.zeros(pridePop)
    maleNomadIndicies = np.zeros(nomadPop)

    # the number of expected males in the population of prides and nomads
    noPrideMales = int(round(pridePop * (1 - sexRate), 0))
    noNomadMales = int(round(nomadPop * sexRate, 0))

    # generate bit array with correct no of males
    for i in range(noPrideMales):
        malePrideIndicies[i] = 1

    for i in range(noNomadMales):
        maleNomadIndicies[i] = 1

    # mix up the distribution of males a bit
    random.shuffle(maleNomadIndicies)
    random.shuffle(malePrideIndicies)


    ''' generating lions into the structures '''
    # init arrays of nomad and pride lions
    nomadLionsArray = np.array([Lion() for i in range(nomadPop)])
    prideLionsArray = np.array([Lion() for i in range(pridePop)])


    # set attributes for nomad lions
    for i in range(nomadPop):

        nomadLionsArray[i].isNomad = True

        # set gender of nomad lions
        if maleNomadIndicies[i] == 1:
            nomadLionsArray[i].isMale = True
        else:
            nomadLionsArray[i].isMale = False


    # init array of prideNo pride groups
    prideArray = np.array([Group(True) for i in range(prideNo)])

    for i in range(pridePop):

        prideLionsArray[i].isNomad = False

        # set gender of pride lions
        if malePrideIndicies[i] == 1:
            prideLionsArray[i].isMale = True
        else:
            prideLionsArray[i].isMale = False


        ''' assigning each pride lion to a pride '''
        # index of pride to assign lion
        # eg for 4 prides, number is 0,1,2,3
        prideIndex = np.random.randint(0, prideNo)
        print(prideIndex)

        prideArray[prideIndex].lionArray = np.append(prideArray[prideIndex].lionArray,
                                                     prideLionsArray[i])

    ''' initialize lion positions'''
    for pride in prideArray:
        for lion in pride.lionArray:
            lion.x = np.random.uniform(0, 1, (1, dim))
            lion.bestVisitedPosition = lion.x

    for lion in nomadLionsArray:
        lion.x = np.random.uniform(lower_limit, upper_limit, (1, dim))
        lion.bestVisitedPosition = lion.x
        
        prideIndex = random.randint(0, prideNo - 1)
        prideArray[prideIndex].lionArray = np.append(prideArray[prideIndex].lionArray, prideLionsArray[i])

    return prideArray, nomadLionsArray


def hunting(pride):
    huntgroup1 = np.array([])
    huntgroup2 = np.array([])
    huntgroup3 = np.array([])
    
    for lion in len(pride.lionArray):
        # 0 is not in group, 1, 2, 3 correspond to respective hunting groups
        if lion.isMale == False:
            lion.huntinggroup = 0
        else:
            lion.huntinggroup = np.random.randint(0, 3)
            
    

# represents a pride or a nomad group
class Group:

    def __init__(self, isPride):

        self.isPride = isPride
        self.lionArray = np.array([])


class Lion:

    def __init__(self):
        
        self.isMale = None
        self.bestVisitedPosition = None
        self.bestVisitedPositionScore = None
        self.groupID = None             # id of the pride or nomad of the Lion
        self.strength = None
        self.isMature = None
        self.isNomad = None
        self.x = None
        self.huntinggroup = None
