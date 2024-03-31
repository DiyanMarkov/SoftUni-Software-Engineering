function solve(number) {

    let numberAsString = number.toString();
    let even = 0;
    let odd = 0;

    for (const digit of numberAsString) {
        currentDigit = Number(digit)

        if (currentDigit % 2 === 0) {
            even += currentDigit
        } else {
            odd += currentDigit
        }

    } 

    console.log(`Odd sum = ${odd}, Even sum = ${even}`)
}

solve(1000435)