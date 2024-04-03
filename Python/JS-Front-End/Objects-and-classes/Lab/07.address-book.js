function addressBook(array) {

    const obj = {};
    

    for (const person of array) {
        [personName, address] = person.split(':');
        obj[personName] = address;

        
    }
    const peopleNames = Object.entries(obj);
    const sortedObj = peopleNames.sort();

    for (const [key,value] of peopleNames) {
        console.log(`${key} -> ${value}`);
    }
    
}

addressBook(['Tim:Doe Crossing',

'Bill:Nelson Place',

'Peter:Carlyle Ave',

'Bill:Ornery Rd'])