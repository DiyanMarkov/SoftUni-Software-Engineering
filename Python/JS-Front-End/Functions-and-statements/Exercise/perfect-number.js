function solve(number) {

    let perfectNum = 0;

    for (let index = 1; index < number; index++) {

        if (number % index === 0) {
            perfectNum += index
        }
        
    }

    if (number === perfectNum) {
        console.log("We have a perfect number!")
    } else {
        console.log("It's not so perfect.");
    }
}

solve(123);