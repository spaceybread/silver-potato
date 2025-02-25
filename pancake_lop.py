def check(arr):
    return any(arr[i] > arr[i + 1] for i in range(len(arr) - 1))

def find_largest_out_of_place(arr):
    largest_idx = -1
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            largest_idx = i if largest_idx == -1 or arr[i] > arr[largest_idx] else largest_idx

    if largest_idx == -1:
        return -1, -1
    
    correct_pos = max(j for j in range(largest_idx + 1, len(arr)) if arr[j] < arr[largest_idx])

    return largest_idx, correct_pos

def sort_lop(arr):
    fc = 0

    while check(arr):
        p, q = find_largest_out_of_place(arr)
        if p != -1:
            arr[p:q+1] = reversed(arr[p:q+1])
            fc += 1  

    return arr, fc
