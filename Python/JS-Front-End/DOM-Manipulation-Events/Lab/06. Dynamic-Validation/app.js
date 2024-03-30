function validate() {
    let input = document.getElementById('email');
    let regex = /^[a-z]+@[a-z]+\.[a-z]+$/gm;
    
    input.addEventListener('change', onChange);

    function onChange(e) {
        let target = e.currentTarget;
        let result = regex.test(target.value)
        
        if (!result) {
            target.classList.add('error')
        } else {
            target.classList.remove('error')
        }
    }
}