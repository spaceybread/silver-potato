def check(arr):
    return any(arr[i] > arr[i + 1] for i in range(len(arr) - 1))

def find_longest_decreasing(arr):
    max_len = 0
    best_p, best_q = -1, -1
    p = 0

    while p < len(arr) - 1:
        if arr[p] > arr[p + 1]:
            q = p
            while q < len(arr) - 1 and arr[q] > arr[q + 1]:  
                q += 1

            if q - p + 1 > max_len: 
                max_len = q - p + 1
                best_p, best_q = p, q

            p = q  
        p += 1

    return best_p, best_q


def sort_lds(arr):
    fc = 0

    while check(arr):
        p, q = find_longest_decreasing(arr)
        if p != -1:
            arr[p:q+1] = reversed(arr[p:q+1])
            fc += 1  

    return arr, fc
