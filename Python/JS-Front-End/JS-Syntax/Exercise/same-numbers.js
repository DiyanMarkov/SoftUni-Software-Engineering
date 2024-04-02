function solve(number) {

    let numberAsString = number.toString();
    let currentDigit = numberAsString[0]
    let areSameDigits = true;
    let sum = Number(currentDigit);

    for (let i=1; i<numberAsString.length; i++) {
        sum += Number(numberAsString[i])

        if (currentDigit !== numberAsString[i]) {
            areSameDigits = false;
        }

    }

    console.log(areSameDigits);
    console.log(sum)
}

solve(2222222);