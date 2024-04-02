// Declaring variables

let a = 10;
let b = 20;
console.log(a+b)  

// Conditional Statements

if (a <= 10) {
    console.log('a is lower than or equal to 10');
} else if (a < 20) {
    console.log('a is lower than 20');
} else {
    console.log('a is higher than 20');
}

// Fuction Declaration

function addNubmers (first, second) {
    console.log(first + second)
}

// Function Invoke

addNubmers(15, 4);

// Concatenation

console.log('The number pi is: ' + 3.14 + '!')
console.log(`The number pi is: ${3.14}!!`)

// For loops

for (let i = 10; i > 0; i-=1) {
    console.log(i)
}

// While loops

let i = 8

while (i > 5) {
    console.log(`The number is ${i}`)
    i-=1
}

function multiply (number) {
    console.log(number * 2)
}

multiply(2)

function solve(m, n) {
    for (let i=m; i >= n; i--) {
        console.log(i)
    }
}

solve(6,2)