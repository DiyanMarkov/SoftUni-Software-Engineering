window.addEventListener("load", solve);

function solve() {
    let placeInput = document.querySelector('#place');
    let actionInput = document.querySelector('#action');
    let personInput = document.querySelector('#person');

    let taskList = document.querySelector('#task-list');
    let doneList = document.querySelector('#done-list')

    let addBtn = document.querySelector('#add-btn');

    addBtn.addEventListener('click', (e) => {

        if (!personInput.value || !actionInput.value || !personInput.value) {
            return;
        }

        let place = placeInput.value;
        let action = actionInput.value;
        let person = personInput.value;

        let li = document.createElement('li');
        li.className = 'clean-task';

        let article = document.createElement('article');

        let pPlace = document.createElement('p');
        pPlace.textContent = `Place:${placeInput.value}`;

        let pAction = document.createElement('p');
        pAction.textContent = `Action:${actionInput.value}`;

        let pPerson = document.createElement('p');
        pPerson.textContent = `Person:${personInput.value}`;

        let divContainerBtns = document.createElement('div');
        divContainerBtns.className = 'buttons';

        let editBtn = document.createElement('button');
        editBtn.className = 'edit';
        editBtn.textContent = 'Edit';

        editBtn.addEventListener('click', (e) => {
            placeInput.value = place;
            actionInput.value = action;
            personInput.value = person;
            
            li.remove();
        })

        let doneBtn = document.createElement('button');
        doneBtn.className = 'done';
        doneBtn.textContent = 'Done';

        doneBtn.addEventListener('click', (e) => {
            editBtn.remove();
            doneBtn.remove();

            let deleteBtn = document.createElement('button');
            deleteBtn.className = 'delete';
            deleteBtn.textContent = 'Delete'; 

            deleteBtn.addEventListener('click', (e) => {
                li.remove();
            });

            li.appendChild(deleteBtn);
            
            doneList.appendChild(li);

        });

        divContainerBtns.appendChild(editBtn);
        divContainerBtns.appendChild(doneBtn);

        article.appendChild(pPlace);
        article.appendChild(pAction);
        article.appendChild(pPerson);

        li.appendChild(article);
        li.appendChild(divContainerBtns);

        taskList.appendChild(li);

        clearForm();

    });

    function clearForm() {
        placeInput.value = '';
        actionInput.value = '';
        personInput.value = '';     
    }
}