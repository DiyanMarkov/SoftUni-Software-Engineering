function sumTable() {
    let products = document.getElementsByTagName('tr');
    let sum = 0;

    for (let index = 1; index < products.length; index++) {
        let cells = products[index].children;
        cellPrice = Number(cells[1].textContent);
        sum += cellPrice
        
    }

    document.getElementById('sum').textContent = sum
    
}