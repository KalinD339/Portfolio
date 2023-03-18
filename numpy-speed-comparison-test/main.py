import numpy as np
from numpy import random as nprn
import random as rnd
import time
import math
"""
Creates matrixes, using numpy and for-cycles,
does mathematical calculations on them through
the numpy module, then multiplies them 2 by 2,
until there is only 1 matrix left, cube roots
it. Configurable number of matrixes, their d-s,
maximum number in each matrix and total iters.
"""
MATRIXES = 256 # must be power of 2
SIZE_OF_MATR = 100
MAX_NUMB = 10000
ITERATIONS = 100

def create_numpy_matrixes():
    nump_arrays = []
    for a in range(MATRIXES):
        nump_arrays.append(nprn.randint(MAX_NUMB, size=(SIZE_OF_MATR,SIZE_OF_MATR)))
    nump_matr = np.array(nump_arrays)
    return nump_matr

def create_normal_matrixes():
    matrixes = []
    for matrix in range(MATRIXES):
        temp_matr = []
        for a in range(SIZE_OF_MATR):
            temp_vert = []
            for b in range(SIZE_OF_MATR):
                temp_vert.append(rnd.randint(0, MAX_NUMB))
            temp_matr.append(temp_vert)
        matrixes.append(temp_matr)
    return matrixes

def multiply_matrixes(matrixes):
    temp_matr = matrixes
    for a in temp_matr:
        a = np.cbrt(np.power(a, 5))
    while len(temp_matr) != 1:
        calc_matr = []
        for a in range(len(temp_matr)//2):
            calc_matr.append(np.multiply(matrixes[a*2], matrixes[a*2+1]))
        temp_matr = calc_matr
    temp_matr = np.cbrt(temp_matr)


def main():
    start_time = time.time()
    for a in range(ITERATIONS):
        nump_matr = create_numpy_matrixes()
        multiply_matrixes(nump_matr)
    print("--- %s seconds for numpy ---" % (time.time() - start_time))

    start_time = time.time()
    for a in range(ITERATIONS):
        normal_matr = create_normal_matrixes()
        multiply_matrixes(normal_matr)
    print("--- %s seconds for normal matrix ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()
