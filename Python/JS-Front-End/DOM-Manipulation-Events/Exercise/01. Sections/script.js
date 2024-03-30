function create(words) {
   
   const parentDiv = document.getElementById('content');

   for (const word of words) {
      let newDiv = document.createElement('div');
      let newParagraph = document.createElement('p');
      parentDiv.appendChild(newDiv);
      newDiv.appendChild(newParagraph);

      newParagraph.textContent = word;
      newParagraph.style.display = 'none';

      newDiv.addEventListener('click', display);

      function display(e) {
         newParagraph.style.display = '';
      }
      
   }
   
}