test = [6,2,4,3,1,5,0,23,75,1,-55,-125,85,34,534]

def selectionSort(arr):
    x = 1
    for i in range(len(arr)-2):
        # print("\n","*"*50, "\niteration", i)
        min = i
        for j in range(x, len(arr)):
            # print("comparing", arr[i], arr[j])
            if arr[min] > arr[j]:
                min = j
                # print("min is: ", arr[min])
        x += 1
        arr[i], arr[min] = arr[min], arr[i]
    return arr

print(selectionSort(test))
