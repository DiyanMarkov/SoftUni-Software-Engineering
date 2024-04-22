const baseUrl = 'http://localhost:3030/jsonstore/games'

let loadGamesBtn = document.querySelector('#load-games');


let gamesList = document.querySelector('#games-list')

let formElement = document.querySelector('#form-section')

const nameInput = document.querySelector('#g-name')
const typeInput = document.querySelector('#type')
const playersInput = document.querySelector('#players')

const formAddBtn = document.querySelector('#add-game')
const formEditBtn = document.querySelector('#edit-game')

loadGamesBtn.addEventListener('click', loadGames);

formAddBtn.addEventListener('click', (e) => {
    e.preventDefault();
    // create the vacation from the input

    let newGame = {
        name: nameInput.value,
        type: typeInput.value,
        players: playersInput.value
    }


    // POST request to the server
    fetch(baseUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(newGame)   
    })
        .then(loadGames) // kogato uspeshno resolve-nesh fetch-a na POST-a --> Load-ni vsichki vacations
    // POST + GET request
    clearForm();
});

formEditBtn.addEventListener('click', (e) => {
    e.preventDefault();

    // get id
    const gameId = formElement.dataset.game;

    const gameData = {
        _id: gameId,
        name: nameInput.value,
        type: typeInput.value,
        players: playersInput.value
    };

    //put request

    fetch(`${baseUrl}/${gameId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(gameData)
    })
        .then(loadGames) // load vacations
        .then(() => {

            // actiavate add button
            formAddBtn.removeAttribute('disabled');

            // deactivate edit button
            formEditBtn.setAttribute('disabled', 'disabled')

            // clear form
            clearForm();

            // delete id 
            delete formElement.dataset.game;
        });
});

function loadGames() {
    return fetch(baseUrl)
        .then(res => res.json())
        .then(result => {
            renderGames(Object.values(result));
        });
}

function clearForm() {
    nameInput.value = '';
    typeInput.value = '';
    playersInput.value = '';
}

function renderGames(games) { // render-ira vsicki vacation-i

    gamesList.innerHTML = '';

    games
        .map(game => renderGame(game)) // .map(renderVacation)
        .forEach(game => gamesList.appendChild(game));
}

function renderGame(game) { // render-ira edinichen vacation

    let container = document.createElement('div');
    container.className = 'content';

    let pName = document.createElement('p');
    pName.textContent = game.name;

    let pPlayers = document.createElement('p');
    pPlayers.textContent = game.players;

    let pType = document.createElement('p');
    pType.textContent = game.type;

    let buttonsContainer = document.createElement('div');
    buttonsContainer.className = 'buttons-container';

    let boardGame = document.createElement('div');
    boardGame.className = 'board-game';

    let changeBtn = document.createElement('button');
    changeBtn.className = 'change-btn';
    changeBtn.textContent = 'Change';
    changeBtn.addEventListener('click', (e) => {
        // add to form fields
        nameInput.value = game.name;
        typeInput.value = game.type;
        playersInput.value = game.players;
        
        // remove from confirmed list
        container.remove();
        // Activate edit vacation button
        formEditBtn.removeAttribute('disabled');
        // deactivate add vacation button
        formAddBtn.setAttribute('disabled', true);

        // save id
        formElement.dataset.game = game._id;
    })

    let deleteBtn = document.createElement('button');
    deleteBtn.className = 'delete-btn';
    deleteBtn.textContent = 'Delete';

    deleteBtn.addEventListener('click', (e) => {
        // send delete request
        fetch(`${baseUrl}/${game._id}`, {
            method: 'DELETE'
        })
            // load vacations
            .then(loadGames)
    })

    container.appendChild(pName);
    container.appendChild(pPlayers);
    container.appendChild(pType);

    buttonsContainer.appendChild(changeBtn);
    buttonsContainer.appendChild(deleteBtn);

    boardGame.appendChild(container);
    boardGame.appendChild(buttonsContainer);

    gamesList.appendChild(boardGame);

    return boardGame;

}