function solve(product, quantity) {
    const coffee = 1.50;
    const water = 1.00;
    const coke = 1.40;
    const snacks = 2.00;

    let result;

    switch (product) {
        case 'coffee':
            result = coffee * quantity;
            break;
        case 'water':
            result = water * quantity;
            break;
        case 'coke':
            result = coke * quantity;
            break;
        case 'snacks':
            result = snacks * quantity;
            break;
    }

    console.log(result.toFixed(2))
}

solve('water', 5);
solve('coffee', 2);