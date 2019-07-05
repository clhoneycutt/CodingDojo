test = [6,2,4,3,1,5,0,23,75,1,-55,-125,85,34,534]


def insertSort(arr):
    for i in range(1,len(arr)):
        print("\n","*"*50, "\niteration: ","i is ", i)
        for j in range(i-1,-1,-1):
            below = j - 1
            print("comparing","arr[j] is ",arr[j], "arr[i] is ",arr[i])
            if arr[i] > arr[j]:
                print("higher")
            elif arr[i] < arr[j]:
                print("lower. inserting", arr[j])
                temp = arr.pop(j)
                arr.insert(below, temp)
    return arr


            
        







print(insertSort(test))