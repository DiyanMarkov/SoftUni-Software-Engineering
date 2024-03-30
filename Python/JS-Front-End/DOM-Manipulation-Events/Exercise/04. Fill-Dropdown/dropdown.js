function addItem() {
    let text = document.getElementById('newItemText');
    let valueText = document.getElementById('newItemValue');

    let select = document.querySelector('#menu');
    let option = document.createElement('option');

    option.textContent = text.value;
    option.value = valueText.value;
    select.appendChild(option);

    text.value = '';
    valueText.value = '';
}