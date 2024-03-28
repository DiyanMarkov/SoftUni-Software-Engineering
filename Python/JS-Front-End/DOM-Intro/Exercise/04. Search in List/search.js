function search() {
   let listItems = document.querySelectorAll('li');
   let searchingText = document.getElementById('searchText').value;
   let result = document.getElementById('result');
   let matches = 0;

   for (const town of Array.from(listItems)) {
      town.style.fontWeight = '';
      town.style.textDecoration = '';
   }

   for (const town of Array.from(listItems)) {
      if (town.textContent.includes(searchingText)) {
         matches++;
         town.style.fontWeight = 'bold';
         town.style.textDecoration = 'underline';
      }
   }

   result.textContent = `${matches} matches found`



}
