function solve(type, weightAsGrams, pricePerkg) {
    let weightInKg = weightAsGrams / 1000;
    totalMoney = weightInKg * pricePerkg;
    console.log(`I need $${totalMoney.toFixed(2)} to buy ${weightInKg.toFixed(2)} kilograms ${type}.`);
}

solve('orange', 2500, 1.80);