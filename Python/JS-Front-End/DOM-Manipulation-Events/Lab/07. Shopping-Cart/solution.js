function solve() {
   let buttons = Array.from(document.querySelectorAll('button.add-product'));
   let checkoutBtn = document.querySelector('button.checkout');
   let textArea = document.querySelector('textarea');
   

   let boughtProducts = [];
   let totalPrice = 0;

   for (const button of buttons) {
      button.addEventListener('click', onClick);
   }
   

   function onClick(e) {
      let productDiv = e.currentTarget.parentNode.parentNode;
      let productTitle = productDiv.querySelector('.product-title').textContent;
      let productPrice = productDiv.querySelector('.product-line-price').textContent;

      if (!boughtProducts.includes(productTitle)) {
         boughtProducts.push(productTitle)
      }

      totalPrice += Number(productPrice);
      textArea.value += `Added ${productTitle} for ${productPrice} to the cart.\n`

   }

   checkoutBtn.addEventListener('click', checkout);

   function checkout(e) {
      textArea.value += `You bought ${boughtProducts.join(', ')} for ${totalPrice.toFixed(2)}.`
      buttons.forEach(button => {
         button.removeEventListener('click', onClick)
      });
   }
}