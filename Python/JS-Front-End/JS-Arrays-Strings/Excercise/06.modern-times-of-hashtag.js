function solve(text) {
    let regex = /#[A-Za-z]+/g;

    let matches = text.match(regex);

    for (let word of matches) {
        word = word.replace('#', '')
        console.log(word)
    }
}

solve('Nowadays everyone uses # to tag a #special word in #socialMedia')