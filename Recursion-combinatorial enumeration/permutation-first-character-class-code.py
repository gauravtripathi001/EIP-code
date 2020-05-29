def perm(arr):
    results = []
    perm_util(arr, 0, results)
    print(results)

def perm_util(arr, i, result):
    if i == len(arr):
        result.append(arr.copy())
        return
    for j in range(i, len(arr)):
        arr[i], arr[j] = arr[j], arr[i]
        perm_util(arr, i+1, result)
        arr[i], arr[j] = arr[j], arr[i]

perm([1,2,3])
