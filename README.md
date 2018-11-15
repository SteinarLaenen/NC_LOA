# NC_LOA

Assignment Natural Computing

Based on:
Maziar Yazdani and Fariborz Jolai. “Lion optimization algorithm (LOA): a nature-inspired
metaheuristic algorithm”. In: Journal of computational design and engineering 3.1 (2016),
pp. 24–36.

# LOA
The main engine of the algorithm is the LOA_main file. In here the parameters are define and the iterative process is implemented, and the results are collected.

To run the LOA algorithm: 
run python LOA_main.py

Make sure to set the desired parameters and evaluation function beforehand.
The results are saved in two .npy files.

## lib
The intricacies of the algorithm can be found in the LOA_lib file. In here we implement the details in the algorithm subroutines. The methods here are called from with the LOA_main file. In here we have for example, manipulate the lions to mate and produce cubs, the initialisation of the first population etc.

In the benchmark file we define our evaluation functions. These are called from within the LOA_main file and passed to the Lion objects in the LOA_lib file for evaluation. Our benchmark functions are based on the CEC guideline.


# PSO
In the PSO file we implement the PSO algorithm. This calls on the benchmark file to evaluate the progress throughout its iterations.

to run PSO:
python PSO.py

Make sure to set desired parameters and benchmark evaluation function beforehand.
The result is saved in a .npy file.

# Results

The results of our experiments can be found in the results folder. To plot the results run: python plot.py

