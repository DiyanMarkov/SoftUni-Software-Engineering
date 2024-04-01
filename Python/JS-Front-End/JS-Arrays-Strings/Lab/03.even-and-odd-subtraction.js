function solve(arrayOfNumbers) {
    let evenNums = 0;
    let oddNums = 0;

    for (let number of arrayOfNumbers) {
        if (number % 2 === 0) {
            evenNums += number
        } else {
            oddNums += number
        }
    }

    result = evenNums - oddNums
    console.log(result)
}

solve([1,2,3,4,5,6])