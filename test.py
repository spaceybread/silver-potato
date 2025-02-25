from pancake_lds import *
from pancake_lop import *
from pancake import *
import random
import sys

N = int(sys.argv[1])

res_n = []
res_l = []
res_o = []
for _ in range(N):
    test_list = random.sample(range(1, 10001), 100)
    sol = sorted(test_list)
    cann, fcn = sort(test_list[:])
    canl, fcl = sort_lds(test_list[:])
    cano, fco = sort_lop(test_list[:])
    
    if sol != cann or sol != canl or sol != cano:
        print("Failed:", test_list)
        break
    print("Flips:", fcn, fcl, fco)
    res_n.append(fcn)
    res_l.append(fcl)
    res_o.append(fco)

print("====== Full Stats ======")
print("Max Naive:", max(res_n))
print("Min Naive:", min(res_n))
print("Avg Naive:", sum(res_n) / N)

print("Max LDS:", max(res_l))
print("Min LDS:", min(res_l))
print("Avg LDS:", sum(res_l) / N)

print("Max LOP:", max(res_o))
print("Min LOP:", min(res_o))
print("Avg LOP:", sum(res_o) / N)


