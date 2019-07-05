li = [8,4,2,5,3,1,0,6,7]

def bubbleSort(arr):
    for j in range(len(arr)-1):
        # print("\n\n", "-"*50, "Iteration", j)
        for i in range(len(arr)-1-j):
            # print("\n", "*"*80, "\ncomparing", arr[i], arr[i+1])
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                # print("swapped", arr[i], arr[i+1])
                # print("array is now", arr)
    return arr
    
        
print(bubbleSort(li))
