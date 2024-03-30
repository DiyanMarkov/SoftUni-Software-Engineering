function addItem() {
    
    let text = document.getElementById('newItemText');
    let li = document.createElement('li');
    li.textContent = text.value;

    let ul = document.getElementById('items');
    ul.appendChild(li);
}