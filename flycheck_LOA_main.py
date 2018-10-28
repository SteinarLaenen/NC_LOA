# Lion Optimisation Algorithm implementation
# Natural computing assignment
# Python3.6.6
# Main LOA engine

# library imports
import LOA_lib


# set algorithm params as global variables
prideNo = 4             # number of pride structures
percentNomad = 0.2      # portion of population to be nomads
roamingPercent = 0.2
mutateProb = 0.2
sexRate = 0.8
mateProb = 0.3
migrateRate = 0.4
nPop = 100
upper_limit = 100
lower_limit = -100
dim = 30

# initialise the populations into structures of prides and nomads
prideArray, nomadLionsArray = LOA_lib.generateGroups(nPop, sexRate, prideNo, percentNomad,
                                                     upper_limit, lower_limit, dim)



#while True:


    #for each pride:
        #some femail go hunting
        #other stuff too

    #for each nomad:
        #move about randomly in search space

    #for each pride again
        #some femail migrate to pride

    # final do: fig 11 step 
