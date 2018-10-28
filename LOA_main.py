# Lion Optimisation Algorithm implementation
# Natural computing assignment
# Python3.6.6
# Main LOA engine

# library imports
import numpy as np

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
