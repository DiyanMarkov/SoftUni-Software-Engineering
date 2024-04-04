window.addEventListener("load", solve);

function solve() {
    
    let student = document.querySelector('#student');
    let university = document.querySelector('#university');
    let score = document.querySelector('#score');
    let nextButton = document.querySelector('#next-btn');
    
    

    nextButton.addEventListener('click', addToPreview);

    
    function addToPreview(e) {

        const studentName = student.value;
        const universityName = university.value;
        const scoreResult = score.value;

        if (!student.value || !university.value || !score.value) {
            return;
        }

        previewListElement = document.querySelector('#preview-list');

        liElement = document.createElement('li');
        liElement.className = 'application';

        article = document.createElement('article');

        h4Element = document.createElement('h4');
        h4Element.textContent = student.value;

        pUniElement = document.createElement('p');
        pUniElement.textContent = `University: ${university.value}`;

        pScoreElement = document.createElement('p');
        pScoreElement.textContent = `Score: ${score.value}`;

        edinBtn = document.createElement('button');
        edinBtn.textContent = 'edit';
        edinBtn.className = 'action-btn';
        edinBtn.classList.add('edit');

        applyBtn = document.createElement('button');
        applyBtn.textContent = 'apply';
        applyBtn.className = 'action-btn';
        applyBtn.classList.add('apply');


        previewListElement.appendChild(liElement);
        liElement.appendChild(article);
        article.appendChild(h4Element);
        article.appendChild(pUniElement);
        article.appendChild(pScoreElement);
        liElement.appendChild(edinBtn);
        liElement.appendChild(applyBtn);


        nextButton.setAttribute('disabled', true);

        student.value = '';
        university.value = '';
        score.value = '';


        edinBtn.addEventListener('click', (e) => {
            let currentLi = e.currentTarget.parentNode.parentNode;

            student.value = studentName;
            university.value = universityName;
            score.value = scoreResult;

            currentLi.remove();
            nextButton.removeAttribute('disabled');
        });

        applyBtn.addEventListener('click', (e) => {
            let currentLi = e.currentTarget.parentNode;
            edinBtn.remove();
            applyBtn.remove();

            let candidatesList = document.querySelector('#candidates-list');
            candidatesList.appendChild(currentLi);

            nextButton.removeAttribute('disabled');
            
        })


    }
    

  }
  