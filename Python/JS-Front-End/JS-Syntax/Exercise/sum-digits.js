function solve(number) {
    let text = number.toString();

    let sum = 0;

    for (i=0; i < text.length; i++) {
        sum += Number(text[i]);
    }

    console.log(sum);
}

solve(245678);