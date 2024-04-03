function piccolo(array) {

    let carNumbers = [];

    for (const car of array) {
        let [direction, plateNumber] = car.split(', ');
        
        if (direction === 'IN' && !carNumbers.includes(plateNumber)) {
            carNumbers.push(plateNumber)
            
        } else if (direction === 'OUT' && carNumbers.includes(plateNumber)) {
            let index = carNumbers.indexOf(plateNumber);
            carNumbers.splice(index, 1);
        }

    }


    if (carNumbers.length > 0) {
        let sortedPlates = carNumbers.sort((a,b) => a.localeCompare(b))
        console.log(sortedPlates.join("\r\n"));
    } else {
        console.log('Parking Lot is Empty');
    }  
}

piccolo(['IN, CA2844AA', 'IN, CA1234TA', 'OUT, CA2844AA', 
'IN, CA9999TT', 'IN, CA2866HI', 'OUT, CA1234TA', 
'IN, CA2844AA', 'OUT, CA2866HI', 'IN, CA9876HH', 
'IN, CA2822UU'])