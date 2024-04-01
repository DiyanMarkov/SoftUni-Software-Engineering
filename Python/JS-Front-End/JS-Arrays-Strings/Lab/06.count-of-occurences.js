function solve(sentence, word) {
    let result = sentence.split(' ')
    let occurences = 0;


    for (substring of result) {
        if (substring === word) {
            occurences += 1
        }
    }

    console.log(occurences)
}

solve('This is a word and it also is a sentence', 'is')