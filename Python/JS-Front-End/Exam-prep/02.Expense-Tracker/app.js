window.addEventListener("load", solve)

function solve() {

    let addBtn = document.querySelector('#add-btn');
    let expenseInput = document.querySelector('#expense');
    let amountInput = document.querySelector('#amount');
    let dateInput = document.querySelector('#date');

    addBtn.addEventListener('click', (e) => {
        e.preventDefault();
        
        if (!expenseInput.value || !amountInput.value || !dateInput.value) {
            return;
        }

        const date = dateInput.value;
        const amount = amountInput.value;
        const expense = expenseInput.value;

        let previewList = document.querySelector('#preview-list');
        let expenseList = document.querySelector('#expenses-list')

        let li = document.createElement('li');
        li.className = 'expense-item';

        let article = document.createElement('article');

        let pType = document.createElement('p');
        pType.textContent = `Type: ${expenseInput.value}`;

        let pAmount = document.createElement('p');
        pAmount.textContent = `Amount: ${amountInput.value}$`;

        let pDate = document.createElement('p');
        pDate.textContent = `Date: ${dateInput.value}`;

        let divContainerButtons = document.createElement('div');
        divContainerButtons.className = 'buttons';

        let editBtn = document.createElement('button');
        editBtn.classList.add('btn');
        editBtn.classList.add('edit');
        editBtn.textContent = 'edit';

        editBtn.addEventListener('click', (e) => {
            e.preventDefault();

            expenseInput.value = expense;
            amountInput.value = amount;
            dateInput.value = date;

            let currentLi = e.currentTarget.parentNode.parentNode;
            
            currentLi.remove();

            addBtn.removeAttribute('disabled')
        });

        let okBtn = document.createElement('button');
        okBtn.classList.add('btn');
        okBtn.classList.add('ok');
        okBtn.textContent = 'ok';

        okBtn.addEventListener('click', (e) => {
            currentLi = e.currentTarget.parentNode.parentNode;

            editBtn.remove();
            okBtn.remove();

            expenseList.appendChild(currentLi);

            addBtn.removeAttribute('disabled')
        });

        let deleteBtn = document.querySelector('.btn.delete');

        deleteBtn.addEventListener('click', (e) => {
            location.reload();
        })


        divContainerButtons.appendChild(editBtn);
        divContainerButtons.appendChild(okBtn);

        article.appendChild(pType);
        article.appendChild(pAmount);
        article.appendChild(pDate);

        li.appendChild(article);
        li.appendChild(divContainerButtons);

        previewList.appendChild(li);

        addBtn.setAttribute('disabled', true);

        expenseInput.value = '';
        amountInput.value= '';
        dateInput.value= '';

        
    })


}