function solve(array) {

    array.sort((a,b) => {
        return a.localeCompare(b);
    })

    let index = 1;

    for (let name of array) {
        console.log(`${index}.${name}`)
        index++;
    }
}

solve(["John", "Bob", "Christina", "Ema"])