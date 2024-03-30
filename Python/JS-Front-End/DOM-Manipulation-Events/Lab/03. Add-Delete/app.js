function addItem() {
    let text = document.getElementById('newItemText');
    let li = document.createElement('li'); //Parent element
    li.textContent = text.value;

    let ul = document.getElementById('items');
    ul.appendChild(li);

    let deleteLink = document.createElement('a'); // Create link
    deleteLink.textContent = '[Delete]'; // Give the link a text
    deleteLink.href = '#'; // Create new class with name -> href and value -> #

    li.appendChild(deleteLink) // Append the deleteLink to Parent element 'li' 

    deleteLink.addEventListener('click', deleteItem)// Event Registration to the 'deleteLink ref'
    
    function deleteItem (e) { // 'e' -> event has all information
        target = e.currentTarget.parentNode; // the target we need to remove (the parent (li) of (a) link)
        target.remove(); // remove target
    }

    text.value = '';
}