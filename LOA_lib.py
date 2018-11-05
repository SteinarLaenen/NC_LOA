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



def hunting(prideArray):

    for pride in prideArray:
        # assign lion to a hunting group
        for lion in pride.lionArray:
            # 0 is not in group, 1, 2, 3 correspond to respective hunting groups
            if lion.isMale == True:        # male lions do not hunt
                lion.huntingGroup = 0
            else:
                lion.huntingGroup = np.random.randint(0, 4)

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

        # hunting females all attack the prey
        # first set center group to be the group with max fitness, left and right groups are two
        # lower fitness groups
        fitnesses = [huntingGroup1Fitness, huntingGroup2Fitness, huntingGroup3Fitness]
        centre = np.argsort(fitnesses)[0]
        right = np.argsort(fitnesses)[1]
        left = np.argsort(fitnesses)[2]

        for lion in pride.lionArray:
            ## Change of lion position depends if they are in left or right group
            ##FIX ISSUE WITH BOUNDS
            if lion.huntingGroup == centre:
                lion.x = np.random.uniform(preyPosition, lion.x)
            if (lion.huntingGroup == right):
                lion.x = np.random.uniform(preyPosition, 2*preyPosition - lion.x)
            if (lion.huntingGroup == left):
                lion.x = np.random.uniform(2*preyPosition - lion.x, preyPosition)
            
            if lion.getBestVisitedPositionScore() > lion.getCurrentPositionScore():
                # get the improvement percentage
                improvement_percentage = lion.getBestVisitedPositionScore()/lion.getCurrentPositionScore()
                print(improvement_percentage)
                lion.bestVisitedPosition = lion.x
                # change the position of the prey according to Opposition Based Learning
                preyPosition = preyPosition + np.random.uniform(0, 1) * improvement_percentage * (preyPosition - lion.x)
        print(preyPosition)

    return prideArray

def moveToSafePlace(prideArray):
    """
    params:
    input: prideArray
    output: prideArray

    The input should be a pride that has recently gone hunting
    this funciton will take the female lions that have not gone hunting
    and based on a tournament selection strategy, moves them into the direction
    of a better location
    """
    for pride in prideArray:
        # the number of lions that have improved in the previous iteration
        numberImprovedLions = sum([1 for lion in pride.lionArray if lion.bestScoreHistory[-1] < lion.bestScoreHistory[-2]])

        # compute tournament size 
        tournamentsize = max([2, int(np.ceil(numberImprovedLions/2))])

        # best visited positions and their scores in one list
        bestVisitedPositions = [(lion.bestVisitedPosition, lion.getBestVisitedPositionScore()) for lion in pride.lionArray]
        
        for lion in pride.lionArray:
            # if the female is not hunting
            if lion.huntingGroup == 0 and lion.isMale == False:

                # tournament selection
                tournamentSelection = random.sample(bestVisitedPositions, tournamentsize)
                winner = min(tournamentSelection,key=lambda item:item[1])[0]
                
                R1 = (winner.T).reshape(len(winner.T),)
                startposition = (lion.x.T).reshape(len(lion.x.T),)
                R1 = R1 - startposition
                

                #some parameters for moving the female non-hunting lion
                D = np.linalg.norm(lion.x - R1)

                # create random orthonormal vector to R1
                R2 = np.random.randn(len(R1.T))
                R2 -= R2.dot(R1) * R1 / np.linalg.norm(R1)**2

                #HOW DO WE PICK?
                theta = 0

                lion.x = lion.x + 2*np.random.uniform(0,1)*R1 + \
                         np.random.uniform(-1, 1) * np.tan(theta) *  R2

                
    return prideArray


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
# def step6(prideArray, nomadLionsArray, nPop, sexRate, percentNomad):

#     # list of male and female lions sorted by strength
#     maleNomads = [lion for lion in nomadLionsArray if lion.isMale == True].sort(key lambda lion: lion.getCurrentPositionScore())
#     femaleNomads = [lion for lion in nomadLionsArray if lion.isMale == False].sort(key lambda lion: lion.getCurrentPositionScore())


#     ''' adding fittest female nomads to a pride with spare capacity '''
#     # while there are still some empty places in a pride due to migration
#     # add a female lion to the pride based on fitness
#     while not(nonFullPrides(prideArray) == set()):

#         # get indicies of prides which have spare capacity
#         nonFullPrideIndicies = nonFullPrides(prideArray)

#         # select at random a pride to add a lion
#         prideIndex = random.sample(nonFullPrideIndicies, 1)

#         # add fittest female to the pride
#         prideArray[prideIndex].lionArray = np.append(prideArray[prideIndex].lionArray, femaleNomads[0])
#         del femaleNomads[0]


#     ''' removing the least fit nomads '''
#     # to remain consistent max number of each gender in nomad population
#     maxMaleNomadNo = nPop * percentNomad * sexRate
#     maxFemaleNomadNo = nPop * percentNomad * (1 - sexRate)

#     # if number of male nomads is greater than that permitted
#     # remove the least fittest
#     while len(maleNomads) > maxMaleNomadNo:
#         del maleNomads[-1]

#     while len(femaleNomads) > maxFemaleNomadNo:
#         del femaleNomads[-1]

#     # collect surviving lions together
#     remainingNomadLions = np.concatenate((femaleNomads, maleNomads))


#     return prideArray, remainingNomadLions


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
        # ie for 4 prides: [0,1,1,0] means attack the prides 2 and 3 only
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


def updateBestScoreList(prideArray, nomadLionsArray):
    """
    function to update the list of best scores obtained by each lion.
    This is done for tournament selection in hunting
    """
    for pride in prideArray:
        for lion in pride.lionArray:
            lion.bestScoreHistory.append(lion.getBestVisitedPositionScore())

    for lion in nomadLionsArray:
        lion.bestScoreHistory.append(lion.getBestVisitedPositionScore())
        
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
        self.bestScoreHistory = [np.Infinity]      # keep track of best score found so far for tournament


    # fitness value of best visited position
    def getBestVisitedPositionScore(self):
        return self.evaluation(self.bestVisitedPosition)


    # fitness value of current position
    def getCurrentPositionScore(self):
        return self.evaluation(self.x)
