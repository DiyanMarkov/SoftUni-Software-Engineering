const baseUrl = 'http://localhost:3030/jsonstore/tasks';

let locationInput = document.querySelector('#location');
let temperatureInput = document.querySelector('#temperature');
let dateInput = document.querySelector('#date');

let addWeatherBtn = document.querySelector('#add-weather');
let editWeatherBtn = document.querySelector('#edit-weather');

let weatherList = document.querySelector('#list');
let form = document.querySelector('#form form');

let loadHistoryBtn = document.querySelector('#load-history');

loadHistoryBtn.addEventListener('click', loadHistory);

addWeatherBtn.addEventListener('click', (e) => {
    e.preventDefault();

    let newWeather = {
        date: dateInput.value,
        location: locationInput.value,
        temperature: temperatureInput.value
    }

    fetch(baseUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(newWeather)

    })
        .then(loadHistory)

    clearForm();
        
});

editWeatherBtn.addEventListener('click', (e) => {
    e.preventDefault();

    const weatherId = form.dataset.town;

    let townData = {
        _id: weatherId,
        date: dateInput.value,
        location: locationInput.value,
        temperature: temperatureInput.value
    }

    fetch(`${baseUrl}/${weatherId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(townData)
    })
        .then(loadHistory)
        .then(() => {

            editWeatherBtn.setAttribute('disabled', true);
            addWeatherBtn.removeAttribute('disabled');

            clearForm()

            delete form.dataset.town
        })
       
});

function loadHistory() {
    return fetch(baseUrl)
        .then(res => res.json())
        .then(result => {
            renderWeathers(Object.values(result))
        });
}

function renderWeathers(towns) {

    weatherList.innerHTML = '';

    towns
        .map(renderWeather)
        .forEach(town => weatherList.appendChild(town));
}

function renderWeather(town) {
    let container = document.createElement('div');
    container.className = 'container';

    let h2 = document.createElement('h2');
    h2.textContent = town.location;

    let h3Date = document.createElement('h3');
    h3Date.textContent = town.date;

    let h3Temperature = document.createElement('h3');
    h3Temperature.setAttribute("id", "celsius");
    h3Temperature.textContent = town.temperature;

    let divButtonsContainer = document.createElement('div');
    divButtonsContainer.className = 'buttons-container';

    let changeBtn = document.createElement('button');
    changeBtn.className = 'change-btn';
    changeBtn.textContent = 'Change';

    changeBtn.addEventListener('click', (e) => {

        locationInput.value = town.location;
        temperatureInput.value = town.temperature;
        dateInput.value = town.date;

        editWeatherBtn.removeAttribute('disabled');
        addWeatherBtn.setAttribute('disabled', true);

        container.remove()

        // save id

        form.dataset.town = town._id

        });

    let deleteBtn = document.createElement('button');
    deleteBtn.className = 'delete-btn';
    deleteBtn.textContent = 'Delete';

    deleteBtn.addEventListener('click', (e) => {
        fetch(`${baseUrl}/${town._id}`, {
            method: 'DELETE'
        })
            .then(loadHistory)

        clearForm();
    });

    divButtonsContainer.appendChild(changeBtn);
    divButtonsContainer.appendChild(deleteBtn);

    container.appendChild(h2);
    container.appendChild(h3Date);
    container.appendChild(h3Temperature);
    container.appendChild(divButtonsContainer);

    return container;

}

function clearForm() {
    locationInput.value= '';
    temperatureInput.value = '';
    dateInput.value = '';
    
}