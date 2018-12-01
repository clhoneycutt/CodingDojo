def selectionSort(arr):
    x = 1
    min = arr[0]
    for i in range(len(arr)-1):
        for j in range(x, len(arr)-1):
            