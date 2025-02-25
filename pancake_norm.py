def flip(arr, k: int) -> None:
    left = 0
    while left < k:
        arr[left], arr[k] = arr[k], arr[left]
        k -= 1
        left += 1

def max_index(arr, k: int) -> int:
    index = 0
    for i in range(k):
        if arr[i] > arr[index]:
            index = i
    return index

def sort_norm(arr) -> None:
    n = len(arr)
    fc = 0
    while n > 1:
        maxidx = max_index(arr, n)
        if maxidx != n - 1:
            if maxidx != 0:
                flip(arr, maxidx)
                fc += 1
            flip(arr, n - 1)
            fc += 1
        n -= 1
    return fc
