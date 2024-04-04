const baseUrl = 'http://localhost:3030/jsonstore/tasks';

let foodInput = document.querySelector('#food');
let timeInput = document.querySelector('#time');
let caloriesInput = document.querySelector('#calories');

let addMealBtn = document.querySelector('#add-meal');
let editMealBtn = document.querySelector('#edit-meal');

let mealList = document.querySelector('#list');
let form = document.querySelector('#form form');

let loadMealBtn = document.querySelector('#load-meals');

loadMealBtn.addEventListener('click', loadMeal);

addMealBtn.addEventListener('click', (e) => {
    e.preventDefault();

    let newMeal = {
        calories: caloriesInput.value,
        food: foodInput.value,
        time: timeInput.value
    }

    fetch(baseUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(newMeal)

    })
        .then(loadMeal)

    clearForm();
        
});

editMealBtn.addEventListener('click', (e) => {
    e.preventDefault();

    const mealId = form.dataset.meal;

    let mealData = {
        _id: mealId,
        calories: caloriesInput.value,
        food: foodInput.value,
        time: timeInput.value
    }

    fetch(`${baseUrl}/${mealId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(mealData)
    })
        .then(loadMeal)
        .then(() => {

            editMealBtn.setAttribute('disabled', true);
            addMealBtn.removeAttribute('disabled');

            clearForm()

            delete form.dataset.meal
        })
       
});

function loadMeal() {
    return fetch(baseUrl)
        .then(res => res.json())
        .then(result => {
            renderWeathers(Object.values(result))
        });
}

function renderWeathers(meals) {

    mealList.innerHTML = '';

    meals
        .map(renderWeather)
        .forEach(meal => mealList.appendChild(meal));
}

function renderWeather(meal) {
    let container = document.createElement('div');
    container.className = 'meal';

    let h2 = document.createElement('h2');
    h2.textContent = meal.food;

    let h3Time = document.createElement('h3');
    h3Time.textContent = meal.time;

    let h3Calories = document.createElement('h3');
    h3Calories.textContent = meal.calories;

    let divButtonsContainer = document.createElement('div');
    divButtonsContainer.setAttribute("id", "meal-buttons");

    let changeBtn = document.createElement('button');
    changeBtn.className = 'change-meal';
    changeBtn.textContent = 'Change';

    changeBtn.addEventListener('click', (e) => {

        foodInput.value = meal.food;
        timeInput.value = meal.time;
        caloriesInput.value = meal.calories;

        editMealBtn.removeAttribute('disabled');
        addMealBtn.setAttribute('disabled', true);

        container.remove()

        // save id

        form.dataset.meal = meal._id

        });

    let deleteBtn = document.createElement('button');
    deleteBtn.className = 'delete-meal';
    deleteBtn.textContent = 'Delete';

    deleteBtn.addEventListener('click', (e) => {
        fetch(`${baseUrl}/${meal._id}`, {
            method: 'DELETE'
        })
            .then(loadMeal)

        clearForm();
    });

    divButtonsContainer.appendChild(changeBtn);
    divButtonsContainer.appendChild(deleteBtn);

    container.appendChild(h2);
    container.appendChild(h3Time);
    container.appendChild(h3Calories);
    container.appendChild(divButtonsContainer);

    return container;

}

function clearForm() {
    foodInput.value= '';
    timeInput.value = '';
    caloriesInput.value = '';
    
}