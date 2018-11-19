// Biggie Size - Given an array, write a function that changes all positive numbers in the array to "big".  Example: makeItBig([-1,3,5,-5]) returns that same array, changed to [-1, "big", "big", -5].

function makeItBig(arr){
    // iterate through the array
    for (var i = 0; i < arr.length; i++){
        // compare the value to 0 to make sure it's positive
        if (arr[i] > 0){
            // switch value to be 'big'
            arr[i] = "big";
        }
    }
    return arr;
}
// console.log(makeItBig([-1,3,5, 7,-5]));

// Print Low, Return High - Create a function that takes array of numbers.  The function should print the lowest value in the array, and return the highest value in the array.

function printLowReturnHigh(arr){
    var low = arr[0];
    var high = arr[0];
    for (var i = 1; i < arr.length; i++){
        if (arr[i] < low){
            low = arr[i];
        }else if (arr[i] > high){
            high = arr[i];
        }
    }
    console.log(low);
    return high;
}

// console.log(printLowReturnHigh([50,-1,20,12]));

// Print One, Return Another - Build a function that takes array of numbers.  The function should print second-to-last value in the array, and return first odd value in the array.

function print2ndToLastReturnOdd(arr){
    console.log(arr[arr.length-2]);
    for (var i = 0; i < arr.length; i++){
        if (arr[i] % 2 == 1){
            return arr[i];
        }
    }
}
// console.log(print2ndToLastReturnOdd([0,2,1,4,3]));

// Double Vision - Given array, create a function to return a new array where each value in the original has been doubled.  Calling double([1,2,3]) should return [2,4,6] without changing original.

function doubleVision(arr){
    var newArr = [];
    for (var i = 0; i < arr.length; i++){
        newArr.push(arr[i] * 2);
    }
    return newArr;
}
// console.log(doubleVision([1,2,3]));

// Count Positives - Given array of numbers, create function to replace last value with number of positive values.  Example, countPositives([-1,1,1,1]) changes array to [-1,1,1,3] and returns it.

function countPositives(arr){
    var positives = 0;
    for (var i = 0; i < arr.length; i++){
        if (arr[i] > 0){
            positives++;
        }
    }
    arr[arr.length-1] = positives;
    return arr;
}
// console.log(countPositives([1,1,0,0]));

// Evens and Odds - Create a function that accepts an array.  Every time that array has three odd values in a row, print "That's odd!".  Every time the array has three evens in a row, print "Even more so!"

function evensOdds(arr){
    var odds = 0;
    var evens = 0;
    for (var i = 0; i < arr.length; i++){
        if (arr[i] % 2 == 1){
            odds++;
            evens = 0;
        }else{
            evens++;
            odds = 0;
        }
        if (odds == 3){
            console.log("That's odd!");
            odds = 0;
        }else if(evens == 3){
            console.log("Even more so!");
            evens = 0;
        }
    }
}
// evensOdds([1,1,1,2,2,1,1,1])

// Increment the Seconds - Given an array of numbers arr, add 1 to every second element, specifically those whose index is odd (arr[1], [3], [5], etc).  Afterward. console.log each array value and return arr.

function incrementSeconds(arr){
    for(var i = 1; i < arr.length; i+=2){
        arr[i] = arr[i] + 1;
    }
    for(var i = 0; i < arr.length; i++){
        console.log(arr[i]);
    }
    return arr;
}

console.log(incrementSeconds([1,2,3,4,5]));

// Previous Lengths - You are passed an array containing strings.  Working within that same array, replace each string with a number - the length of the string at previous array index - and return the array.  For example, previousLengths(["hello", "dojo", "awesome"]) should return ["hello", 5, 4].




// Add Seven to Most - Build function that accepts array. Return a new array with all values except first, adding 7 to each. Do not alter the original array.




// Reverse Array - Given an array, write a function that reverses values, in-place.  Example: reverse([3,1,6,4,2]) return same array, containing [2,4,6,1,3].  Do this without creating an empty temporary array.  (Hint: you'll need to swap values).




// Outlook: Negative - Given an array, create and return a new one containing all the values of the provided array, made negative (not simply multiplied by -1). Given [1,-3,5], return [-1,-3,-5].




// Always Hungry - Create a function that accepts an array, and prints "yummy" each time one of the values is equal to "food".  If no array elements are "food", then print "I'm hungry" once.




// Swap Toward the Center - Given array, swap first and last, third and third-to-last, etc.  Input[true,42,"Ada",2,"pizza"] becomes ["pizza", 42, "Ada", 2, true].  Change [1,2,3,4,5,6] to [6,2,4,3,5,1].




// Scale the Array - Given an array arr and a number num, multiply all values in arr by num, and return the changed array arr.  For example, scaleArray([1,2,3],3) should return [3,6,9].