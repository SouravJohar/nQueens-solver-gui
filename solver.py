from genes import *
import genes
import time
import sys

popsize = int(sys.argv[1])
genes.N = int(sys.argv[2])
genes.mutationRate = float(sys.argv[3])


# step 1
# create a random population of `popsize` elements
# each element is a representation of the entire NxN chessboard

'''
Consider the following element for N = 3
[
[0, 1, 0],
[1, 0, 0],
[1, 0, 1]
]


1 denotes that a queen is present at the location
0 denotes that the location is empty
'''

population = createPopulation(popsize)
# we now have a population of randomly generated elements


n = 1
# begin the evolution
while True:
    # calculate the fitness of each element in the population
    # fitness ranges from 0 to 1, which is the normalized value of number of conflicts
    fitness = calcFitness(population)

    # find the element with the highest fitness and its fitness value
    fittest = population[fitness.index(max(fitness))]
    print n
    print max(fitness)
    print fittest
    sys.stdout.flush()

    # if solution is found, print it and break
    if max(fitness) == 1.0:
        # print "Solution found in {} generations".format(n)
        # for row in fittest:
        #     print row
        break

    # create a mating pool where fitter elements have a higher probababilty to pass on their genes
    matingPool = createPool(fitness, population)

    # select two elements from the mating pool and partner them for reproduction
    # mutate the child's genes with a fixed probababilty (mutationRate)
    # build a whole new population like this and repeat the evolution process
    for i in range(popsize):
        child = crossOver(matingPool)
        mutatedChild = mutate(child)
        population[i] = mutatedChild

    n += 1
