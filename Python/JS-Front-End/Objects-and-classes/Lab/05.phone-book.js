function phoneBook(arr) {

    const personInfo = {};

    for (const person of arr) {
        [personName, phone] = person.split(' ');
        personInfo[personName] = phone;
    }

    for (const [key, value] of Object.entries(personInfo)) {
        console.log(`${key} -> ${value}`)
    }
}

phoneBook(['Tim 0834212554',

'Peter 0877547887',

'Bill 0896543112',

'Tim 0876566344'])