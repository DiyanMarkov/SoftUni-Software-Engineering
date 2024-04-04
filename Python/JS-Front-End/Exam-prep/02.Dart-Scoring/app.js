window.addEventListener("load", solve);

function solve() {
    let playerInput = document.querySelector('#player');
    let scoreInput = document.querySelector('#score');
    let roundInput = document.querySelector('#round');

    let sureList = document.querySelector('#sure-list')
    let scoreboardList = document.querySelector('#scoreboard-list');

    let addBtn = document.querySelector('#add-btn');
    let clearBtn = document.querySelector('.btn.clear')

    addBtn.addEventListener('click', (e) => {
      e.preventDefault();

      if (!playerInput.value || !scoreInput.value || !roundInput.value) {
          return;
      } 

      const name = playerInput.value;
      const score = scoreInput.value;
      const round = roundInput.value;

      let li = document.createElement('li');
      li.className = 'dart-item';

      let article = document.createElement('article');

      let pName = document.createElement('p');
      pName.textContent = `${playerInput.value}`;

      let pScore = document.createElement('p');
      pScore.textContent = `Score: ${scoreInput.value}`;

      let pRound = document.createElement('p');
      pRound.textContent = `Round: ${roundInput.value}`;

      let editBtn = document.createElement('button');
      editBtn.classList.add('btn');
      editBtn.classList.add('edit');
      editBtn.textContent = 'edit';

      editBtn.addEventListener('click', (e) => {
          playerInput.value = name;
          scoreInput.value = score;
          roundInput.value = round;

          li.remove();

          addBtn.removeAttribute('disabled')
      });

      let okBtn = document.createElement('button');
      okBtn.classList.add('btn');
      okBtn.classList.add('ok');
      okBtn.textContent = 'ok';

      okBtn.addEventListener('click', (e) => {
          currentLi = e.currentTarget.parentNode;
          editBtn.remove();
          okBtn.remove();

          currentLi.remove();
          scoreboardList.appendChild(li);
      });


      article.appendChild(pName);
      article.appendChild(pScore);
      article.appendChild(pRound);

      li.appendChild(article);
      li.appendChild(editBtn);
      li.appendChild(okBtn);

      sureList.appendChild(li)

      clearForm();

      addBtn.setAttribute('disabled', true);
    })

    clearBtn.addEventListener('click', (e) => {
        location.reload();
    })

    function clearForm() {
      playerInput.value = '';
      scoreInput.value = '';
      roundInput.value = '';
      
    }
  }
  