function solve(words, sentence) {

    let array = words.split(', ')
    let arrayLength = array.length

    let sentenceArray = sentence.split(' ')

    for (let i=0; i<arrayLength; i++) {

        for (substring of sentenceArray) {
            if (substring.length === array[i].length && substring === '*'.repeat(substring.length))
                sentence = sentence.replace(substring, array[i])
        }
        
    }

    console.log(sentence)
}

solve('great, learning', 'softuni is ***** place for ******** new programming languages')