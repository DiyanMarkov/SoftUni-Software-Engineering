function extract(id) {

    let text = document.getElementById(id).textContent;
    let pattern = /\(([^)]+)\)/g;
    let result = text.match(pattern)

    return result.join('; ')
}