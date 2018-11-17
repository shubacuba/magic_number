import sys
import numpy
from numpy import long
from tqdm import *

operators = ["+", "-", "*", "/", ""]
tries = 100000
numbersFound: int = 0
sklad_start = 10950
sklad_end = 10970
sklad = numpy.empty(sklad_end-sklad_start+1, dtype=long)

def expression(n):
    string = "1"
    for i in range(2, 10):
        string += operators[n % len(operators)]
        string += str(i)
        n = int(n / len(operators))
    return string

for x in range(sklad_end-sklad_start):
    sklad[x] = -1

x: long
for x in tqdm(range(tries)):
    res = eval(expression(x))
    if res == int(res):
        res: int = int(res)
        if sklad_start <= res <= sklad_end and sklad[res-sklad_start] == -1:
            sklad[res-sklad_start] = x
            numbersFound += 1

sys.stdout.write(" нашли %s чисел \n" % numbersFound)

for x in range(sklad_start, sklad_end+1):
    sys.stdout.write("%s" % x)
    sys.stdout.write(" =")
    if sklad[x-sklad_start] == -1:
        sys.stdout.write(" not found \n")
    else:
        sys.stdout.write(" %s \n" % expression(sklad[x-sklad_start]))
sys.stdout.write(" нашли %s чисел \n" % numbersFound)