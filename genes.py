from random import *
import math
from numpy import interp

N = 0
target = []
mutationRate = 0


def _vertical_elements(element, column):
    vx = []
    for i in range(len(element)):
        for j in range(len(element)):
            if j == column:
                vx.append(element[i][j])
    return vx


def _diagonal_elements(element, row, column):
    sum = row + column
    diff = row - column
    dx = []
    for i in range(len(element)):
        for j in range(len(element)):
            if i + j == sum or i - j == diff:
                dx.append(element[i][j])
    return dx


def calcFitness(population):
    fitness = []
    for element in population:
        conflicts = 1
        v_conflicts = 0
        d_conflicts = 0
        for i in range(len(element)):
            for j in range(len(element)):
                if element[i][j] == 1:
                    v = _vertical_elements(element, j)
                    v_conflicts += sum(v) - 1
                    d = _diagonal_elements(element, i, j)
                    d_conflicts += sum(d) - 1
        conflicts += v_conflicts + d_conflicts
        fitness.append((1.0 / conflicts))
    return fitness


def createPopulation(popsize):
    population = []
    for i in range(popsize):
        element = [[0 for i in range(N)] for j in range(N)]
        population.append(element)
    for i in range(len(population)):
        for j in range(N):
            index = randint(0, N - 1)
            population[i][j][index] = 1
    return population


def createPool(fitness, pop):
    matingPool = []
    maxFitness = max(fitness)
    for i in range(len(fitness)):
        n = interp(fitness[i], [0, maxFitness], [0, 1])
        n = int(math.floor(n * 100))
        for j in range(n):
            matingPool.append(pop[i])
    return matingPool


def crossOver(matingPool):
    partners = sample(matingPool, 2)
    splitPoint = randint(0, N - 1)
    child = partners[0][:splitPoint] + partners[1][splitPoint:]
    return child


def mutate(child):
    for i in range(len(child)):
        if random() < mutationRate:
            new_row = [0 for k in range(len(child))]
            index = randint(0, len(child) - 1)
            new_row[index] = 1
            child[i] = new_row
    return child
