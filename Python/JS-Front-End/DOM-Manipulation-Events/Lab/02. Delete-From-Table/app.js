function deleteByEmail() {
    let tableRows = Array.from(document.querySelectorAll('tbody tr'));
    let input = document.querySelector('input[name="email"]');
    let resultElement = document.querySelector('#result');
    let isRemoved = false;

    for (const row of tableRows) {
        
        let currentElement = row.children[1];
        
        if (currentElement.textContent === input.value) {
            row.remove();
            isRemoved = true;
        }

    }

    if (isRemoved) {
        resultElement.textContent = 'Deleted';
    } else {
        resultElement.textContent = 'Not found.';
    }
}