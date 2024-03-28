

function generateReport() {
    allObjectsAsArray = []; // array of all objects
    personObject = {}; // one person {key: value}
    checkedBoxesIndexes = [];

    let checkAllColumns = document.querySelectorAll('thead tr th input');

    for (let index = 0; index < checkAllColumns.length; index++) {
        checkboxStatus = checkAllColumns[index].checked;

        if (checkboxStatus) {
            checkedBoxesIndexes.push(index)
        }
        
    }

    columnTitles = document.querySelectorAll('thead tr')[0].getElementsByTagName('th');
    rowsCount = document.querySelectorAll('tbody tr').length;

    for (let row = 0; row < rowsCount; row++) {  // every row of the table
        
        checkedBoxesIndexes.forEach(element => { //checked element one by one
            let key = columnTitles[element].textContent.trim().toLowerCase();
            let value = document.querySelectorAll('tbody tr')[row].getElementsByTagName('td')[element].textContent;
            personObject[key] = value;

        });

        allObjectsAsArray.push(Object.assign(personObject));
        personObject = {};

    }

    document.getElementById('output').textContent = JSON.stringify(allObjectsAsArray)

}   
