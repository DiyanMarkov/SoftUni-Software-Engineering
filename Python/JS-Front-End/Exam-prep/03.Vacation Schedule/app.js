const baseUrl = 'http://localhost:3030/jsonstore/tasks'

let loadVacationsBtn = document.querySelector('#load-vacations');
let vacationList = document.querySelector('#list')
let formElement = document.querySelector('#form form')
const nameInput = document.querySelector('#name')
const daysInput = document.querySelector('#num-days')
const dateInput = document.querySelector('#from-date')
const formAddBtn = document.querySelector('#add-vacation')
const formEditBtn = document.querySelector('#edit-vacation')

loadVacationsBtn.addEventListener('click', loadVacations);

formAddBtn.addEventListener('click', (e) => {
    e.preventDefault();
    // create the vacation from the input

    let newVacation = {
        name: nameInput.value,
        days: daysInput.value,
        date: dateInput.value
    }


    // POST request to the server
    fetch(baseUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(newVacation)   
    })
        .then(loadVacations) // kogato uspeshno resolve-nesh fetch-a na POST-a --> Load-ni vsichki vacations
    // POST + GET request
    clearForm();
});

formEditBtn.addEventListener('click', (e) => {
    e.preventDefault();

    // get id
    const vacationId = formElement.dataset.vacation;

    const vacationData = {
        _id: vacationId,
        name: nameInput.value,
        days: daysInput.value,
        date: dateInput.value
    };

    //put request

    fetch(`${baseUrl}/${vacationId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(vacationData)
    })
        .then(loadVacations) // load vacations
        .then(() => {

            // actiavate add button
            formAddBtn.removeAttribute('disabled');

            // deactivate edit button
            formEditBtn.setAttribute('disabled', 'disabled')

            // clear form
            clearForm();

            // delete id 
            delete formElement.dataset.vacation;
        });
});

function loadVacations() {
    return fetch(baseUrl)
        .then(res => res.json())
        .then(result => {
            renderVacations(Object.values(result));
        });
}

function clearForm() {
    nameInput.value = '';
    daysInput.value = '';
    dateInput.value = '';
}

function renderVacations(vacations) { // render-ira vsicki vacation-i

    vacationList.innerHTML = '';

    vacations
        .map(vacation => renderVacation(vacation)) // .map(renderVacation)
        .forEach(vacation => vacationList.appendChild(vacation));
}

function renderVacation(vacation) { // render-ira edinichen vacation

    let container = document.createElement('div');
    container.className = 'container';

    let h2Element = document.createElement('h2');
    h2Element.textContent = vacation.name;

    let h3DateElement = document.createElement('h3');
    h3DateElement.textContent = vacation.date;

    let h3DaysElement = document.createElement('h3');
    h3DaysElement.textContent = vacation.days;

    let changeBtn = document.createElement('button');
    changeBtn.className = 'change-btn';
    changeBtn.textContent = 'Change';
    changeBtn.addEventListener('click', (e) => {
        // add to form fields
        nameInput.value = vacation.name;
        daysInput.value = vacation.days;
        dateInput.value = vacation.date;
        
        // remove from confirmed list
        container.remove();
        // Activate edit vacation button
        formEditBtn.removeAttribute('disabled');
        // deactivate add vacation button
        formAddBtn.setAttribute('disabled', true);

        // save id
        formElement.dataset.vacation = vacation._id;
    })

    let doneBtn = document.createElement('button');
    doneBtn.className = 'done-btn';
    doneBtn.textContent = 'Done';

    doneBtn.addEventListener('click', (e) => {
        // send delete request
        fetch(`${baseUrl}/${vacation._id}`, {
            method: 'DELETE'
        })
            // load vacations
            .then(loadVacations)
    })

    container.appendChild(h2Element);
    container.appendChild(h3DateElement);
    container.appendChild(h3DaysElement);
    container.appendChild(changeBtn);
    container.appendChild(doneBtn);

    return container;

}

