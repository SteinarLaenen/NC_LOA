import os
import numpy as np
from matplotlib import pyplot as plt

# so we can visualise the process over 5%, 10% etc.
bins = np.arange(0,100,5)
progression = np.array([])

binsProgress = {}

for b in bins:
    binsProgress[b] = []            # add the values to array in each bin


# extract data from files
outFiles = os.listdir("OUTS")

for OF in outFiles:

    f = open("OUTS/" + OF).read()

    # initialise progress to 0%
    currentProgress = 0

    for line in f.split("\n"):


        if ("improved" in line):
            score = float(line.split(":")[1].replace(" ", ""))
            binsProgress[currentProgress].append(score)

        if ("Finished" in line):
            progress = float(line.split("%")[1].replace(" ", "")) * 100

            if progress >= currentProgress + 5:
                currentProgress += 5

for key, val in binsProgress.items():
    # mean the improved score in each bin
    progression = np.append(progression, np.mean(val))


bestValue = progression[-1]
stdev = np.std(binsProgress[bins[-1]])

print ("bestValue", bestValue)
print ("stdev", stdev)

plt.plot(bins, progression)
plt.xlabel("percentage through completion")
plt.ylabel("best score so far")
plt.show()
