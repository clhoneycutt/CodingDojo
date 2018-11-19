// Page 16

// ## Setting and Swapping ##


// var myNumber = 42
// var myName = "Chris"
// var temp = ""

// temp = myName
// myName = myNumber
// myNumber = temp



// ## print -52 to 1066 ##


// for (var i = -52;i<1067;i++) {
//     console.log(i);
// }


// ## Don't Worry, Be Happy ##


// function beCheerful() {
//     console.log("good morning!")
// }

// for (var i=1;i<99;i++) {
//     beCheerful()
// }


// ## Multiple of Three - but Not All ##


// for (var i=-300;i<1;i++) {
//     if (i === -3) {
//         continue;
//     }else if (i === -6) {
//         continue;
//     }else
//         console.log(i)
// }


// ## Printing Integers with While ##


// var i = 2000
// while (i<=5280) {
//     console.log(i);
//     i++
// }


// ## You Say It's Your Birthday ##


function myBirthday(num1,num2) {
    if ((num1 === 13 && num2 === 6) || (num1 === 6 && num2 === 13)) {
        console.log("How did you know?")
    }else{
        console.log("Just another day....")
    }
}


// ## Leap Year ##


function leapYear(year) {
    if ((year%400===0) || (year%4===0 && year%100!==0)) {
        return true
    }else
        return false
}


// ## Print and Count ##


// var count=0;
// for (var i=512;i<=4096;i++) {
//     if (i%5===0) {
//         console.log(i)
//         count++
//     }
// }
// console.log("Numbers disivible by 5: " +count)


// ## Multiple of Six ##


// var i=0;
// while(i<60000) {
//     if (i%6===0) {
//         console.log(i)
//     }
//     i++
// }



// ## Counting, the Dojo Way ##


// for (i=1;i<=100;i++) {
//     if (i%5===0 && i%10===0) {
//         console.log("Coding Dojo");
//     }else if (i%5===0) {
//         console.log("Coding");
//     }else{
//         console.log(i)
//     }
// }


// ## What Do You Know ##


function inputOutput() {
    var incoming = prompt("Enter something");
    console.log(incoming)
}



// ## Woah, That Sucker's Huge... ##


// var sum = 0
// for (var i= -299999;i<300000;i=i+2) {
//     sum+=i
// }
// console.log(sum)


// ## Countdown by Fours ##


// for (i=2016;i>0;i--) {
//     if (i%4===0) {
//         console.log(i)
//     }
// }


// ## Flexible Countdown ##


function flexNum(lowNum,highNum,mult) {
    for (var i=highNum;i>lowNum;i--) {
        if (i%mult===0) {
            console.log(i)
        }
    }
}


// ## The Final Countdown ##


function finalCount(param1,param2,param3,param4) {
    if (param2 > param3) {
        while (param2 > param3) {
            if (param2%param1===0 && param2!==param4) {
                console.log(param2);
            }
            param2--
        }
    }else if (param2 < param3) {
        while (param2 < param3) {
            if (param2%param1===0 && param2 !== param4) {
                console.log(param2);
            }
            param2++
        }
    }
}


// page 20 exercises


// ## Countdown ##


function countdown(num) {
    var arr = [];
    var index = 0
    for (var i=num;i>=0;i--) {
        arr[index] = i;
        index++
    }
    return arr
}


// ## Print and Return ##


function printReturn(arr) {
    console.log(arr[0])
    return arr[1];
}


// ## First Plus Length ##


function firstPlusLength(arr) {
    return arr[0] + arr.length;
}


// ## Values Great than Second ##


// var count =0;
// var list = [1,3,5,7,9,13];

// for (var i=0;i<list.length;i++) {
//     if (list[i] > list[1]) {
//         console.log(list[i]);
//         count++
//     }
// }
// console.log(count)



// ## Values Greater than Second, Generalized


function greaterThanSecond(arr) {
    var count = 0;
    for (var i=0;i<=arr.length;i++) {
        if (arr[i] > arr[1]) {
            console.log(arr[i]);
            count++
        }
    }
    return count

}


// ## This Length, That Value ##


function lengthValue(num1, num2) {
    if (num1 === num2) {
        return "Jinx!";
    }else{
        
    }
}


// ## Fit the First Value ##


function firstValue(arr) {
    if (arr[0] > arr.length) {
        return "Too big!";
    }else if (arr[0] < arr.length) {
        return "Too small!";
    }else{
        return "Just right!"
    }
}


function fahrenheitToCelcius(fDegrees) {
    return (fDegrees - 32) * 5/9
}


function celciusToFahrenheit(cDegrees) {
    return (cDegrees * 9 / 5) + 32
}


function meetInTheMiddle() {
    var celc = 200
    while (true) {
        if (celc > -50) {
            fahr = celciusToFahrenheit(celc);
            if (celc === fahr) {
                console.log("Celcius and Fahrenheit meet at " + fahr + " degrees");
                break;
            }else{
                celc-=1
            }
        }else{
            console.log("Fahrenheit and Celcius do not meet at any temperature between 0 - 500 degrees celcius");
            break;
        }
    }
}



// ## Page 22 ##


// ## Biggie Size ##


function makeItBig(arr) {
    var newArr = arr;
    for (var i=0;i<arr.length;i++) {
        if (arr[i] > 0) {
            arr[i] = "big";
        }
    }
    return newArr;
}


// ## Print Low, Return High


function lowHigh(arr) {
    var low = arr[0];
    var high = arr[0];
    for (var i = 1; i<arr.length;i++) {
        if (arr[i] < low) {
            low = arr[i];
        }
        if(arr[i] > high) {
            high = arr[i];
        }
    }
    console.log(low);
    return high
}


// ## Print One, Return Another ##


function oneAnother(arr) {
    var almostLast = arr[arr.length-2];
    console.log(almostLast);
    for (var i = 0;i < arr.length; i++) {
        if (arr[i] % 2 !== 0) {
            return arr[i]
        }
    }
}


// ## Double Vision ##


function doubleVision(arr) {
    newArr = [];
    for (var i = 0 ; i < arr.length ; i++) {
        newArr[i] = arr[i] * 2
    }
    return newArr;
}


// ## Count Positives ##


function countPositives(arr) {
    var count = 0;
    for (var i = 0 ; i < arr.length ; i++) {
        if (arr[i] > 0) {
            count+= 1;
        }
    }
    arr[arr.length-1] = count;
    return arr;
}


// ## Evens and Odds ##


function evensAndOdds(arr) {
    for (var i = 0; i < arr.length ; i++) {
        if ((i+2) >= arr.length){
            break;
        }else if (arr[i] % 2 !== 0 && arr[i+1] % 2 !== 0 && arr[i+2] % 2 !== 0) {
            console.log("That's Odd");
        }else if (arr[i] % 2 === 0 && arr[i+1] % 2 === 0 && arr[i+2] % 2 === 0) {
            console.log("Even more so!");
        }
    }
}


// ## Increment the Seconds ##

function incrementSeconds(arr) {
    for (var i = 0 ; i < arr.length ; i++) {
        if (arr[i] % 2 !== 0) {
            arr[i] += 1;
            console.log(arr[i]);
        }
    }
    return arr;
}


// ## Previous Lengths ##


function prevLength(arr) {
    for (var i = arr.length - 1 ; i >= 0  ; i--) {
        var newArr = arr;
        if (i === 0) {
            newArr[i] = 0;
        }else{        
            newArr[i] = arr[i-1].length;
        }
    }
    return newArr;
}


// ## Add Seven to Most ##


function sevenToMost(arr) {
    newArr = arr;
    for (var i = 1 ; i < arr.length ; i++) {
        newArr[i] += 7;
    }
    return newArr;
}


// ## Reverse Array ##


function reverseArray(arr) {
    newArr = [];
    for (var i = arr.length - 1 ; i >= 0 ; i--) {
        newArr.push(arr[i]);
    }
    return newArr;
}


// ## Outlook: Negative ##


function outlookNegative(arr) {
    newArr = arr;
    for (var i = 0 ; i < arr.length ; i++) {
        if (newArr[i] > 0) {
            newArr[i] -= newArr[i] * 2;
        }
    }
    return newArr;
}


// ## Always Hungry ##


function alwaysHungry(arr) {
    var count = 0
    for (var i = 0 ; i < arr.length ; i++ ) {
        if (arr[i] === "food") {
            console.log("yummy");
            count ++
        }
        
    }
    if (count === 0) {
        console.log("I'm hungry");
    }
}


// ## Swap Toward the Center ##


function swapToCenter(arr) {
    var temp = 0
    var newArr = arr;
    for (var i = 0 ; i < newArr.length ; i++) {
        if (i > arr.length/2) {
            break;
        }
        if (i === 0) {
            temp = newArr[i]
            newArr[i] = newArr[newArr.length-1]
            newArr[newArr.length-1] = temp
        }else if (i % 2 === 0) {
            temp = newArr[i]
            newArr[i] = newArr[newArr.length-(i + 1)]
            newArr[newArr.length-(i + 1)] = temp
        }
    }
    return newArr;
}


// ## Scale the Array


function scaleArray(arr, num) {
    for (var i = 0 ; i < arr.length ; i++) {
        arr[i] = arr[i] * num
    }
    return arr;
}