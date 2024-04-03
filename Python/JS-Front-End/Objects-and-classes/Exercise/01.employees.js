function employees(arr) {

    const obj = {

    }

    for (const name of arr) {
        obj[name] = name.length;
    }

    for (const [key, value] of Object.entries(obj)) {
        console.log(`Name: ${key} -- Personal Number: ${value}`)
    }
}


employees([
    'Silas Butler',
    'Adnaan Buckley',
    'Juan Peterson',
    'Brendan Villarreal'
    ])