function solve() {
   document.querySelector('#searchBtn').addEventListener('click', onClick);

   function onClick() {
      let input = document.getElementById('searchField');
      let tableRows = document.querySelectorAll('tbody tr');

      console.log(tableRows);

      for (const row of tableRows) {
         row.classList.remove('select');
         if (input.value !== '' && row.textContent.includes(input.value)) {
            row.className = 'select';
         } 
  
      }

      input.value = '';
   }
}