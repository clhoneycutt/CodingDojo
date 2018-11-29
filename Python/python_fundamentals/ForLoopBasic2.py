# Biggie Size - Given an array, write a function that changes all positive numbers in the array to "big". Example: makeItBig([-1, 3, 5, -5]) returns that same array, changed to [-1, "big", "big", -5].

def biggieSize(arr):
    for i in range(len(arr)):
        if arr[i] > 0:
            arr[i] = "big"
    return arr

# Count Positives - Given an array of numbers, create a function to replace last value with number of positive values. Example, countPositives([-1,1,1,1]) changes array to [-1,1,1,3] and returns it.  (Note that zero is not considered to be a positive number).

def countPos(arr):
    pos = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            pos += 1
    arr[len(arr) - 1] = pos
    return arr


# SumTotal - Create a function that takes an array as an argument and returns the sum of all the values in the array.  For example should return 10

def sumTotal(arr):
    total = 0
    for i in range(len(arr)+1):
        total += i
    return total


# Average - Create a function that takes an array as an argument and returns the average of all the values in the array.  For example multiples([1,2,3,4]) should return 2.5

def average(arr):
    total = 0
    for i in range(len(arr) + 1):
        total += i
    return total / len(arr)

# Length - Create a function that takes an array as an argument and returns the length of the array.  For example length([1,2,3,4]) should return 4

def length(arr):
    return len(arr)

# Minimum - Create a function that takes an array as an argument and returns the minimum value in the array.  If the passed array is empty, have the function return false.  For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.

def minimum(arr):
    min = arr[0]
    if len(arr) < 1:
        return False
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
    return min

# Maximum - Create a function that takes an array as an argument and returns the maximum value in the array.  If the passed array is empty, have the function return false.  For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.

def maximum(arr):
    max = arr[0]
    if len(arr) < 1:
        return False
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max

# UltimateAnalyze - Create a function that takes an array as an argument and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the array.

def ultAnalyze(arr):
    result = {'sumTotal': 0, 
            'average': 0, 
            'minimum': arr[0], 
            'maximum': arr[0], 
            'length': len(arr)}
    for i in range(len(arr)):
        result['sumTotal'] += arr[i]
        if arr[i] < result['minimum']:
            result['minimum'] = arr[i]
        elif arr[i] > result['maximum']:
            result['maximum'] = arr[i]
    result['average'] = result['sumTotal'] / len(arr)
    return result


# ReverseList - Create a function that takes an array as an argument and return an array in a reversed order.  Do this without creating an empty temporary array.  For example reverse([1,2,3,4]) should return [4,3,2,1]. This challenge is known to appear during basic technical interviews.

def reverseList(arr):
    lateIndex = len(arr) - 1
    for i in range(len(arr)):
        if i == lateIndex:
            break
        elif i == lateIndex + 1:
            break
        else:
            arr[i], arr[lateIndex] = arr[lateIndex], arr[i]
            lateIndex -= 1
    return arr
