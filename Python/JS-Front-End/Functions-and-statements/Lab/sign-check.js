function solve(numOne, numTwo, numThree) {
    const res = numOne * numTwo * numThree

    if (res >= 0) {
        console.log('Positive')
    } else {
        console.log('Negative')
    }

}

solve(5, 12, -15)