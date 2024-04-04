const baseUrl = 'http://localhost:3030/jsonstore/gifts';

let giftInput = document.querySelector('#gift');
let forInput = document.querySelector('#for');
let priceInput = document.querySelector('#price');

let addPresentBtn = document.querySelector('#add-present');
let editPresentBtn = document.querySelector('#edit-present');

let giftList = document.querySelector('#gift-list');
let form = document.querySelector('#form form');

let loadPresentsBtn = document.querySelector('#load-presents');

loadPresentsBtn.addEventListener('click', loadPresents);

addPresentBtn.addEventListener('click', (e) => {
    e.preventDefault();

    let newGift = {
        price: priceInput.value,
        gift: giftInput.value,
        for: forInput.value
    }

    fetch(baseUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(newGift)

    })
        .then(loadPresents)

    clearForm();
        
});

editPresentBtn.addEventListener('click', (e) => {
    e.preventDefault();

    const giftId = form.dataset.gift;

    let giftData = {
        _id: giftId,
        price: priceInput.value,
        gift: giftInput.value,
        for: forInput.value
    }

    fetch(`${baseUrl}/${giftId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(giftData)
    })
        .then(loadPresents)
        .then(() => {

            editPresentBtn.setAttribute('disabled', true);
            addPresentBtn.removeAttribute('disabled');

            clearForm()

            delete form.dataset.gift
        })
       
});

function loadPresents() {
    return fetch(baseUrl)
        .then(res => res.json())
        .then(result => {
            renderGifts(Object.values(result))
        });
}

function renderGifts(gifts) {

    giftList.innerHTML = '';

    gifts
        .map(renderGift)
        .forEach(gift => giftList.appendChild(gift));
}

function renderGift(gift) {

    let container = document.createElement('div');
    container.className = 'gift-sock';

    let content = document.createElement('div');
    content.className = 'content';

    let pPresent = document.createElement('p');
    pPresent.textContent = gift.gift;

    let pFor = document.createElement('p');
    pFor.textContent = gift.for;

    let pPrice= document.createElement('p');
    pPrice.textContent = gift.price;

    let divButtonsContainer = document.createElement('div');
    divButtonsContainer.className = 'buttons-container';

    let changeBtn = document.createElement('button');
    changeBtn.className = 'change-btn';
    changeBtn.textContent = 'Change';

    changeBtn.addEventListener('click', (e) => {

        giftInput.value = gift.gift;
        forInput.value = gift.for;
        priceInput.value = gift.price;

        editPresentBtn.removeAttribute('disabled');
        addPresentBtn.setAttribute('disabled', true);

        container.remove()

        // save id

        form.dataset.gift = gift._id

        });

    let deleteBtn = document.createElement('button');
    deleteBtn.className = 'delete-btn';
    deleteBtn.textContent = 'Delete';

    deleteBtn.addEventListener('click', (e) => {
        fetch(`${baseUrl}/${gift._id}`, {
            method: 'DELETE'
        })
            .then(loadPresents)

        clearForm();
    });

    divButtonsContainer.appendChild(changeBtn);
    divButtonsContainer.appendChild(deleteBtn);

    content.appendChild(pPresent);
    content.appendChild(pFor);
    content.appendChild(pPrice);
    
    container.appendChild(content);
    container.appendChild(divButtonsContainer);

    return container;

}

function clearForm() {
    giftInput.value= '';
    forInput.value = '';
    priceInput.value = '';
    
}