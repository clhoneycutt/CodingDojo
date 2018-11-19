// Get 1 to 255 - Write a function that returns an array with all the numbers from 1 to 255.
function buildArr(){
    var arr = [];
    for (var i = 1; i <= 255; i++){
        arr.push(i);
    }
    return arr;
}

var result = buildArr(); // <========>
// console.log(result);

// Get even 1000 - Write a function that would get the sum of all the even numbers from 1 to 1000.  You may use a modulus operator for this exercise.
function getSum(){
    var sum = 0;
    for (var i = 1; i <= 1000; i++){
        if (i % 2 == 0){
            sum = sum + i;
        } 
    }
    return sum;
}
// console.log(getSum());


// Sum odd 5000 - Write a function that returns the sum of all the odd numbers from 1 to 5000. (e.g. 1+3+5+...+4997+4999).
function getSumOdd(){
    var sum = 0;
    for (var i = 1; i <= 5000; i+=2){
        if (i % 2 == 1){
            sum = sum + i;
            console.log(i);
        }
    }
    return sum;
}
// console.log(getSumOdd());


// Iterate an array - Write a function that returns the sum of all the values within a given array. (e.g. [1,2,5] returns 8. [-5,2,5,12] returns 14).
function iterate(numArr){
    var sum = 0;
    for (var i = 0; i < numArr.length; i++){
        sum = sum + numArr[i];
    }
    return sum;
}
// console.log(iterate([1,2,4]));


// Find max - Given an array with multiple values, write a function that returns the maximum number in the array. (e.g. for [-3,-5,-6,-2] max is 7)
function findMax(numArr){
    var max = numArr[0]; // sets the maximum to the first value in the array
    for (var i = 0; i < numArr.length; i++){ // for loop to examine each value in the array
        // see if the next value is bigger than the maximum
        if (numArr[i] > max){
            // if it is, make it the new max
            max = numArr[i];
        }
    }
    return max;
}
// console.log(findMax([-3,-5,-6,-2]));

// Find average - Given an array with multiple values, write a function that returns the average of the values in the array. (e.g. for [1,3,5,7,20] average is 7.2)
function findAvg(numArr){
    var sum = 0;
    var avg = 0;
    for (var i = 0; i < numArr.length; i++){
        sum = sum + numArr[i];
    }
    avg = sum / numArr.length;
    return avg;
}
// console.log(findAvg([1,3,5,7,20]));


// Array odd - Write a function that would return an array of all the odd numbers between 1 to 50. (ex. [1,3,5, .... , 47,49]). Hint: Use 'push' method.
function oddArray(){
    var arr = [];
    for (var x = 1; x < 50; x+=2){
        arr.push(x);
    }
    return arr;
}
// oddArray();


// Greater than Y - Given value of Y, write a function that takes an array and returns the number of values that are greater than Y. For example if arr = [1, 3, 5, 7] and Y = 3, your function will return 2. (There are two values in the array greater than 3, which are 5, 7).
function greaterThanY(arr, y){
    var counter = 0;
    // iterate through the array
    for (var idx = 0; idx < arr.length; idx++){
        // check if value in array is greater than y
        if (arr[idx] > y){
            // if it is, counter goes up
            counter++;
        }
    }
    return counter;
}
// console.log(greaterThanY([1,3,5,7], 2));


// Squares - Given an array with multiple values, write a function that replaces each value in the array with the product of the original value squared by itself. (e.g. [1,5,10,-2] will become [1,25,100,4])
function squares(arr){
    for (var idx = 0; idx < arr.length; idx++){
        // square each value and reassign that new value to that index
        arr[idx] = arr[idx]*arr[idx];
    }
}
// squares([1, -2, 5, 10]);

// Negatives - Given an array with multiple values, write a function that replaces any negative numbers within the array with the value of 0. When the program is done the array should contain no negative values. (e.g. [1,5,10,-2] will become [1,5,10,0])
function noNegatives(arr){
    for (var idx = 0; idx < arr.length; idx++){
        // examine each value and see if it's negative.
        if (arr[idx] < 0){
            arr[idx] = 0;
        }
    }
    console.log(arr);
}
// noNegatives([-1,2,-5]);


// Max/Min/Avg - Given an array with multiple values, write a function that returns a new array that only contains the maximum, minimum, and average values of the original array. (e.g. [1,5,10,-2] will return [10,-2,3.5])
function maxMinAvg(arr){
    var sum = 0;
    var max = arr[0];
    var min = arr[0];
    for (var idx = 0; idx < arr.length; idx++){
        sum = sum + arr[idx];
        if (arr[idx] > max){
            max = arr[idx];
        }
        else if (arr[idx] < min){
            min = arr[idx];
        }
    }
    var newArr = [];
    newArr.push(max);
    newArr.push(min);
    var avg = sum/arr.length
    newArr.push(avg);

    return newArr;
}
// console.log(maxMinAvg([2,10,-3,4]));



// Swap Values - Write a function that will swap the first and last values of any given array. The default minimum length of the array is 2. (e.g. [1,5,10,-2] will become [-2,5,10,1]).
function swap(arr){
    var temp = arr[arr.length-1];
    arr[arr.length-1] = arr[0];
    arr[0] = temp;
}
var tester = [1,4,10,-2];
swap(tester);
console.log(tester);




// Number to String - Write a function that takes an array of numbers and replaces any negative values within the array with the string 'Dojo'. For example if array = [-1,-3,2], your function will return ['Dojo','Dojo',2].
function noNegativesDojo(arr){
    for (var idx = 0; idx < arr.length; idx++){
        // examine each value and see if it's negative.
        if (arr[idx] < 0){
            arr[idx] = "Dojo";
        }
    }
    console.log(arr);
}
// noNegativesDojo([-1,2,-5]);