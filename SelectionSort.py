arr = [9,7,4,2,3,1,8,1]

def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_val = i
        for j in range(i, n):
            if arr[j] < arr[min_val]:
                min_val = j
        arr[i], arr[min_val] = arr[min_val], arr[i]
    print(arr)

selectionSort(arr)
