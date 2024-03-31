function solve(number) {
    function singleRow (number) {
        return (number.toString() + ' ').repeat(number)
    }

    for (let index = 1; index <= number; index++) {
        console.log(singleRow(number))     
    }
}

solve(3);