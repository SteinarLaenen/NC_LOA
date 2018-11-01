# Lion Optimisation Algorithm implementation
# Natural computing assignment
# Python3.6.6
# Auxiliary script for main LOA engine

# library imports
import numpy as np
import random
import copy


# initialises a population of lions based on the parameters specified
# and partitions them into the pride and nomad structures
def generateGroups(nPop, sexRate, prideNo, percentNomad, upper_limit, lower_limit, dim, evaluation):

    # expected number of lions in each structure
    nomadPop = int(round(nPop * percentNomad, 0))
    pridePop = nPop - nomadPop


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
        nomadLionsArray[i].evaluation = evaluation
        nomadLionsArray[i].isMature = True

        # set gender of nomad lions
        if maleNomadIndicies[i] == 1:
            nomadLionsArray[i].isMale = True
        else:
            nomadLionsArray[i].isMale = False

        # initialize lion positions
        nomadLionsArray[i].x = np.random.uniform(lower_limit, upper_limit, (1, dim))
        nomadLionsArray[i].bestVisitedPosition = nomadLionsArray[i].x


    # init array of prideNo pride groups
    prideArray = np.array([Group(True) for i in range(prideNo)])

    for i in range(pridePop):

        prideLionsArray[i].isNomad = False
        prideLionsArray[i].isMature = True
        prideLionsArray[i].evaluation = evaluation

        # set gender of pride lions
        if malePrideIndicies[i] == 1:
            prideLionsArray[i].isMale = True
        else:
            prideLionsArray[i].isMale = False

        # initialize lion positions
        prideLionsArray[i].x = np.random.uniform(lower_limit, upper_limit, (1, dim))
        prideLionsArray[i].bestVisitedPosition = prideLionsArray[i].x


        ''' assigning each pride lion to a pride '''
        # index of pride to assign lion
        # eg for 4 prides, number is 0,1,2,3
        prideIndex = np.random.randint(0, prideNo)

        prideArray[prideIndex].lionArray = np.append(prideArray[prideIndex].lionArray, prideLionsArray[i])


    return prideArray, nomadLionsArray



def hunting(pride):

    # assign lion to a hunting group
    for lion in pride.lionArray:

        # 0 is not in group, 1, 2, 3 correspond to respective hunting groups
        if lion.isMale == False:        # male lions do not hunt
            lion.huntingGroup = 0
        else:
            lion.huntingGroup = np.random.randint(0, 3)

    huntingGroup1Fitness = np.sum([lion.getCurrentPositionScore() for lion in pride.lionArray if lion.huntingGroup == 1])
    huntingGroup2Fitness = np.sum([lion.getCurrentPositionScore() for lion in pride.lionArray if lion.huntingGroup == 2])
    huntingGroup3Fitness = np.sum([lion.getCurrentPositionScore() for lion in pride.lionArray if lion.huntingGroup == 3])


    ''' set position of prey to average of hunter positions '''
    preyPosition = np.zeros(len(pride.lionArray[0].x))      # initialize prey position

    hunterLionNumber = 0            # count the number of hunter lions in the pride

    for lion in pride.lionArray:
        if not(lion.huntingGroup == 0):

            preyPosition = np.add(preyPosition, lion.x)     # add the positions within each basis
            hunterLionNumber += 1

    # get the average position of the hunter lions
    preyPosition /= hunterLionNumber



# returns a set of the indicies of prides which are not full because females have migrated
# ie (1,3) would indicate the second and fourth pride can have more female lions to replace migrated ones
def nonFullPrides(prideArray):

    nonFullPrideIndicies = set()
    for i in range(len(prideArray)):
        if not(prideArray[i].migratedFemaleNo == 0):
            nonFullPrideIndicies.add(i)

    return nonFullPrideIndicies


# move some female nomad lions to a pride which has spare capacity
# prides have spare capacity as a result of prior female migration
# remove the weakest lions to remain consistent with permitted number for each gender
def step6(prideArray, nomadLionsArray, nPop, sexRate, percentNomad):

    # list of male and female lions sorted by strength
    maleNomads = [lion for lion in nomadLionsArray if lion.isMale == True].sort(key lambda lion: lion.getCurrentPositionScore())
    femaleNomads = [lion for lion in nomadLionsArray if lion.isMale == False].sort(key lambda lion: lion.getCurrentPositionScore())


    ''' adding fittest female nomads to a pride with spare capacity '''
    # while there are still some empty places in a pride due to migration
    # add a female lion to the pride based on fitness
    while not(nonFullPrides(prideArray) == set()):

        # get indicies of prides which have spare capacity
        nonFullPrideIndicies = nonFullPrides(prideArray)

        # select at random a pride to add a lion
        prideIndex = random.sample(nonFullPrideIndicies, 1)

        # add fittest female to the pride
        prideArray[prideIndex].lionArray = np.append(prideArray[prideIndex].lionArray, femaleNomads[0])
        del femaleNomads[0]


    ''' removing the least fit nomads '''
    # to remain consistent max number of each gender in nomad population
    maxMaleNomadNo = nPop * percentNomad * sexRate
    maxFemaleNomadNo = nPop * percentNomad * (1 - sexRate)

    # if number of male nomads is greater than that permitted
    # remove the least fittest
    while len(maleNomads) > maxMaleNomadNo:
        del maleNomads[-1]

    while len(femaleNomads) > maxFemaleNomadNo:
        del femaleNomads[-1]

    # collect surviving lions together
    remainingNomadLions = np.concatenate((femaleNomads, maleNomads))


    return prideArray, remainingNomadLions


# nomad lions moving randomly in the search space
def nomadsRoam(nomadLionsArray, lower_limit, upper_limit, dim):

    for lion in nomadLionsArray:

        # best position of all nomad lions
        bestPosition = np.min([lion.x for lion in nomadLionsArray])

        # the max threshold number in order for the lion to roam
        thresholdRoamingProbability = 0.1 + np.min(0.5, (lion.x - bestPosition) / bestPosition)

        # move lion if not greater than the threshold
        if not(random.random() > thresholdRoamingProbability):
             lion.x = np.random.uniform(lower_limit, upper_limit, (1, dim))

             # update the best visited position if better than current
            if lion.getBestVisitedPositionScore() < lion.getCurrentPositionScore():
                lion.bestVisitedPosition = lion.x


    return nomadLionsArray


# male nomad lions attack a resident male of a pride
# resident males are places depending on which lion is stronger
def nomadsAttackPride(prideArray, nomadLionsArray):

    for nomadInd in range(len(nomadLionsArray)):

        # skip if nomad is female
        if nomadLionsArray[nomadInd].isMale == False:
            continue

        # generate binary array with length of number of prides
        # ie for 4 prides: [0,1,1,0], 1 means attack the pride
        pridesToAttack = [random.randint(0, 1) for i in range(len(prideArray))]

        # for each pride
        for prideInd in range(len(prideArray)):

            # attack pride
            if pridesToAttack[prideInd] == 1:

                # get resident lion from the pride
                maleIndex = [mInd for mInd in range(len(prideArray[prideInd].lionArray)) if prideArray[prideInd].lionArray[mInd].isMale == True][0]
                residentLion = prideArray[prideInd].lionArray[maleIndex]

                # get the nomad lion to contest
                nomadLion = nomadLionsArray[nomadInd]

                # if the nomad is stronger than the resident
                if nomadLion.getCurrentPositionScore() > residentLion.getCurrentPositionScore():

                    # create a temporary resident lion object copy
                    residentLionCopy = copy.deepcopy(residentLion)

                    # replace resident with nomad
                    residentLion = nomadLion

                    # replace nomad with copy of resident
                    nomadLion = residentLionCopy


    return prideArray, nomadLionsArray



# represents a pride or a nomad group
class Group:

    def __init__(self, isPride):

        self.isPride = isPride
        self.lionArray = np.array([])
        self.migratedFemaleNo = None


class Lion:

    def __init__(self):

        self.isMale = None
        self.evaluation = None
        self.bestVisitedPosition = None
        self.groupID = None             # id of the pride or nomad of the Lion
        self.isMature = None
        self.isNomad = None
        self.x = None
        self.huntingGroup = None


    # fitness value of best visited position
    def getBestVisitedPositionScore(self):
        return self.evaluation(self.bestVisitedPosition)


    # fitness value of current position
    def getCurrentPositionScore(self):
        return self.evaluation(self.x)
