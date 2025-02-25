import random
from pancake import *
from pancake_lds import *
from pancake_lop import *
from pancake_norm import *

def run_fuzzy_test(n, trials=1000):
    naive_results = []
    lds_results = []
    lop_results = []
    nor_results = []

    for _ in range(trials):
        arr = random.sample(range(n * n), n)  # Generate random permutation
        _, flips_naive = sort(arr[:])  # Implement naive sorting
        _, flips_lds = sort_lds(arr[:])  # Implement LDS sorting
        _, flips_lop = sort_lop(arr[:])  # Your LOP
        flips_nor = sort_norm(arr[:])

        if _ != sorted(arr[:]): break
        
        naive_results.append(flips_naive)
        lds_results.append(flips_lds)
        lop_results.append(flips_lop)
        nor_results.append(flips_nor)

    print(f"Avg Naive: {sum(naive_results) / trials}")
    print(f"Avg LDS: {sum(lds_results) / trials}")
    print(f"Avg LOP: {sum(lop_results) / trials}")
    print(f"Avg Nor: {sum(nor_results) / trials}")

run_fuzzy_test(100, trials=100)
