window.addEventListener("load", solve);

function solve() {

    let nameInput = document.querySelector('#name')
    let phoneInput = document.querySelector('#phone')
    let categoryInput = document.querySelector('#category')

    let checkList = document.querySelector('#check-list')
    let contactList = document.querySelector('#contact-list')

    let addBtn = document.querySelector('#add-btn')

    addBtn.addEventListener('click', (e) => {
        e.preventDefault();

        if (!nameInput.value | !phoneInput.value | !categoryInput.value) {
          return;
        }

        let name = nameInput.value;
        let phone = phoneInput.value;
        let category = categoryInput.value;


        let li = document.createElement('li');

        let article = document.createElement('article');

        let pName = document.createElement('p');
        pName.textContent = `name:${nameInput.value}`;

        let pPhone = document.createElement('p');
        pPhone.textContent = `phone:${phoneInput.value}`;

        let pCategory = document.createElement('p');
        pCategory.textContent = `category:${categoryInput.value}`;

        let buttonsContainer = document.createElement('div');
        buttonsContainer.className = 'buttons';

        let editBtn = document.createElement('button');
        editBtn.className = 'edit-btn';

        editBtn.addEventListener('click', (e) => {
            nameInput.value = name;
            phoneInput.value = phone;
            categoryInput.value = category;

            li.remove();
        })

        let saveBtn = document.createElement('button');
        saveBtn.className = 'save-btn';

        saveBtn.addEventListener('click', (e) => {

            let currentLi = e.currentTarget.parentNode.parentNode;
            console.log(currentLi);

            editBtn.remove();
            saveBtn.remove();

            currentLi.remove()

            contactList.appendChild(li)

            deleteBtn = document.createElement('button')
            deleteBtn.className = 'del-btn';
            li.appendChild(deleteBtn)

            deleteBtn.addEventListener('click', (e) => {
                li.remove();
            })
        })

        article.appendChild(pName);
        article.appendChild(pPhone);
        article.appendChild(pCategory);

        buttonsContainer.appendChild(editBtn);
        buttonsContainer.appendChild(saveBtn);

        li.appendChild(article);
        li.appendChild(buttonsContainer);

        checkList.appendChild(li);

        clearForm();

    })

    function clearForm() {
        nameInput.value = '';
        phoneInput.value = '';
        categoryInput.value = '';
    }

  }
  