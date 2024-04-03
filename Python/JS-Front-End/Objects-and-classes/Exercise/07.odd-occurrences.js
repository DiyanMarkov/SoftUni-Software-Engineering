function oddOccurrences(text) {
    let array = text.split(' ');
    
    let oddWords = {};

    for (const word of array) {

        let lowerCaseWord = word.toLowerCase();

        if (!oddWords.hasOwnProperty(lowerCaseWord)) {
            oddWords[lowerCaseWord] = 1
        } else {
            oddWords[lowerCaseWord] += 1
        }
    }

    let filteredWords = [];

    for (const [key, value] of Object.entries(oddWords)) {
        if (value % 2 !== 0) {
            filteredWords.push(key)
        }
    }

    console.log(filteredWords.join(' '));
}

oddOccurrences('Java C# Php PHP Java PhP 3 C# 3 1 5 C#');