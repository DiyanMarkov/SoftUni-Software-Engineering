function convertToObject(json) {
    let obj = JSON.parse(json)

    for (const [key, value] of Object.entries(obj)) {
        console.log(`${key}: ${value}`)
    }
}

convertToObject('{"name": "George", "age": 40, "town": "Sofia"}')