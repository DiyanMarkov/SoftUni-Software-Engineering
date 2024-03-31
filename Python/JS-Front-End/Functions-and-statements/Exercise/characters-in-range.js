function solve(char1, char2) {
    let start = Math.min(char1.charCodeAt(), char2.charCodeAt());
    let end = Math.max(char1.charCodeAt(), char2.charCodeAt());

    let result = '';

    for (let index = start + 1; index < end; index++) {
        result += String.fromCharCode(index) + ' '
    }

    console.log(result.trim())
}

solve('a', 'd');