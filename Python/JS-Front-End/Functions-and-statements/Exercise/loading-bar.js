function solve(number) {
    if (number === 100) {
        console.log('100% Complete!');
    } else {
        repeatNum = number / 10
        console.log(`${number}% [${'%'.repeat(repeatNum)}${'.'.repeat(10 - repeatNum)}]`);
        console.log('Still loading...');
    }

}

solve(30);