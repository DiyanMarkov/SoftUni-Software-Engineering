function storeProvision(currentStock, orderedProducts) {
    
    let obj = {};

    for (let index = 0; index < currentStock.length; index += 2) {
        const product = currentStock[index];
        const quantity = Number(currentStock[index + 1]);
            
        if (obj.hasOwnProperty(product)) {
            obj[product] += quantity
        } else {
            obj[product] = quantity
        }
    }

    for (let index = 0; index < orderedProducts.length; index += 2) {
        const product = orderedProducts[index];
        const quantity = Number(orderedProducts[index + 1]);
            
        if (obj.hasOwnProperty(product)) {
            obj[product] += quantity
        } else {
            obj[product] = quantity
        }
    }

    for (const [key, value] of Object.entries(obj)) {
        console.log(`${key} -> ${value}`);
    }
}

storeProvision(
    [
    'Chips', '5', 'CocaCola', '9', 'Bananas',
    '14', 'Pasta', '4', 'Beer', '2' 
    ],
    
    [ 
    'Flour', '44', 'Oil', '12', 'Pasta', '7',
    'Tomatoes', '70', 'Bananas', '30'
    ]);