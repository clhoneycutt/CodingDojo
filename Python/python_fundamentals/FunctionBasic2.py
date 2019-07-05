# Countdown - Create a function that accepts a number as an input.  Return a new array that counts down by one, from the number (as arrays 'zero'th element) down to 0 (as the last element).  For example countDown(5) should return [5,4,3,2,1,0].

def countdown(num):
    arr = []
    for i in range(num, -1, -1):
        arr.append(i)
    return arr



# Print and Return - Your function will receive an array with two numbers. Print the first value, and return the second.

def printReturn(arr):
    print(arr[0])
    return arr[1]


# First Plus Length - Given an array, return the sum of the first value in the array, plus the array's length.

def firstPlusLength(arr):
    return arr[0] + len(arr)


# Values Greater than Second - Write a function that accepts any array, and returns a new array with the array values that are greater than its 2nd value. 
 
def greaterThanSecond(arr):
    new = []
    for i in range(len(arr)):
        if arr[i] > arr[1]:
            new.append(arr[i])
    return new

# Print how many values this is.  If the array is only one element long, have the function return False

def printVal(arr):
    values = 0
    if len(arr) == 1:
        return False
    else:
        for i in range(len(arr)):
            values += 1
    print(values)



# This Length, That Value - Write a function called lengthAndValue which accepts two parameters, size and value. This function should take two numbers and return a list of length size containing only the number in value. For example, lengthAndValue(4,7) should return [7,7,7,7].

def lengthAndValue(size,value):
    arr = []
    for i in range(size):
        arr.append(value)
    return arr
