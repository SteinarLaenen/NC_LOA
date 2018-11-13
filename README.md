# NC_LOA

Assignment Natural Computing

Based on:
Maziar Yazdani and Fariborz Jolai. “Lion optimization algorithm (LOA): a nature-inspired
metaheuristic algorithm”. In: Journal of computational design and engineering 3.1 (2016),
pp. 24–36.

The main engine of the algorithm is the LOA_main file. In here the parameters are define and the iterative process is implemented, and the results are collected.

The intricacies of the algorithm can be found in the LOA_lib file. In here we implement the details in the algorithm subroutines. The methods here are called from with the LOA_main file. In here we have for example, manipulate the lions to mate and produce cubs, the initialisation of the first population etc.

In the benchmark file we define our evaluation functions. These are called from within the LOA_main file and passed to the Lion objects in the LOA_lib file for evaluation. Our benchmark functions are based on the CEC guideline.

In the PSO file we implement the PSO algorithm. This calls on the benchmark file to evaluate the progress throughout its iterations.
