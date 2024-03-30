function lockedProfile() {
    let buttons = Array.from(document.getElementsByTagName('button'));

    for (const button of buttons) {
        button.addEventListener('click', showMore);

        function showMore(e) {
            let btn = e.currentTarget;
            let profile = btn.parentNode;

            let hiddenElement = profile.getElementsByTagName('div')[0];
            let unlocked = profile.querySelector(('input[value="unlock"]'));
            
            
            if (!unlocked.checked) {
                return;
            }

            if (btn.textContent === 'Show more') {
                hiddenElement.style.display = 'block';
                btn.textContent = 'Hide it';
            } else if (btn.textContent === 'Hide it' && unlocked.checked) {
                btn.addEventListener('click', hideIt);
                
                function hideIt(e) {
                    hiddenElement.style.display = 'none';
                    btn.textContent = 'Show more';
    
                }
                
            }

        }
  
    }

}