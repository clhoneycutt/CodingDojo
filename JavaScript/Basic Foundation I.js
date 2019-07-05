


// 1) Get 1 to 255 - Write a function that returns an array with all the numbers from 1 to 255.


function byteRange(){
    var arr = [];
    for (var i = 1; i<256 ; i++){
        arr.push(i);
    }
    return arr;
}



// 2) Get even 1000 - Write a function that would get the sum of all the even numbers from 1 to 1000.  You may use a modulus operator for this exercise.


function sumOfEven(){
    var sum = 0;
    for (var i = 0;i<=1000;i++){
        if (i % 2 == 0){
            sum += i;
        }
    }
    return sum;
}


// 3) Sum odd 5000 - Write a function that returns the sum of all the odd numbers from 1 to 5000. (e.g. 1+3+5+...+4997+4999).


function sumOfOdd(){
    var sum = 0;
    for (var i = 0; i < 5000; i++){
        if (i % 2 != 0){
            sum += i;
        }
    }
    return sum;
}


// 4) Iterate an array - Write a function that returns the sum of all the values within an array. (e.g. [1,2,5] returns 8. [-5,2,5,12] returns 14).


function sumOfArr(arr){
    var sum = 0;
    for (var i = 0; i < arr.length ; i++){
        sum += arr[i];
    }
    return sum;
}


// 5) Find max - Given an array with multiple values, write a function that returns the maximum number in the array. (e.g. for [-3,3,5,7] max is 7)


function findMax(arr){
    var max = arr[0];
    for (var i = 1 ; i < arr.length ; i++){
        if (arr[i] > max){
            max = arr[i];
        }
    }
    return max;
}


// 6) Find average - Given an array with multiple values, write a function that returns the average of the values in the array. (e.g. for [1,3,5,7,20] average is 7.2)


function findAvg(arr){
    var sum = 0;
    for (var i = 0 ; i < arr.length ; i++){
        sum += arr[i];
    }
    return sum / arr.length;
}


// 7) Array odd - Write a function that would return an array of all the odd numbers between 1 to 50. (ex. [1,3,5, .... , 47,49]). Hint: Use 'push' method.


function returnOdd(arr){
    var newArr = [];
    for (var i = 0 ; i < arr.length ; i++){
        if (arr[i] % 2 != 0){
            newArr.push(arr[i]);
        }
    }
    return newArr;
}


// 8) Greater than Y - Given value of Y, write a function that takes an array and returns the number of values that are greater than Y. For example if arr = [1, 3, 5, 7] and Y = 3, your function will return 2. (There are two values in the array greater than 3, which are 5, 7).


function greaterThanY(arr, y){
    var counter = 0;
    for (var i = 0 ; i < arr.length ; i++){
        if (arr[i] > y){
            counter += 1;
        }
    }
    return "The number of values over " + y + " is: " + counter;
}

// 9) Squares - Given an array with multiple values, write a function that replaces each value in the array with the product of the original value squared by itself. (e.g. [1,5,10,-2] will become [1,25,100,4])


function returnSquares(arr){
    for (var i = 0 ; i < arr.length ; i++) {
        
    }
}