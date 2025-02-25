arr = [5, 3, 2, 1, 6, 7, 0, 4, 9, 8]
sol = sorted(arr)

def check(arr):
    return any(arr[i] > arr[i + 1] for i in range(len(arr) - 1))


def sort(arr):
    fc = 0
    while check(arr):
        inSeq = False
        p = -1
        flipped = False
    
        for i in range(len(arr) - 1):
        
            if arr[i] > arr[i + 1]:
                if inSeq: continue
                else:
                    p = i
                    inSeq = True
            else:
                if inSeq:
                    arr[p:i + 1] = reversed(arr[p:i+1])
                    inSeq = False
                    flipped = True
                    fc += 1
                    break
            
        if inSeq and not flipped:
            arr[p:] = reversed(arr[p:])
            fc += 1    

    return arr, fc

print(sort(arr), sort(arr) == sol)
