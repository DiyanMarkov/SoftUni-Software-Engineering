function solve(word, text) {

    let textArray = text.toLowerCase().split(' ');


    for (let i=0; i<textArray.length; i++) {

        if (textArray[i] === word) {
            return console.log(word)
        }

    }

    console.log(`${word} not found!`)


}

solve('javascript', 'JavaScript is the best programming language')