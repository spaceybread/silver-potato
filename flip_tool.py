import sys
N = int(sys.argv[1])
arr = list(range(1, N + 1))
sol = list(range(1, N + 1))

k1, k2 = int(sys.argv[2]), int(sys.argv[3])

i = 0
while True:
    print(arr, i)
    if i % 2 == 0:
        arr = arr[:k1][::-1] + arr[k1:]
    else:
        arr = arr[:k2][::-1] + arr[k2:]
    i += 1

    if arr == sol: break
print(arr, i)
print(i, i // 2)
