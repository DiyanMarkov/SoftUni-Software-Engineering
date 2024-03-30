function focused() {
    let sections = Array.from(document.querySelectorAll('input'));

    for (const section of sections) {

        section.addEventListener('focus', sectionFocuse)
        section.addEventListener('blur', sectionBlur)  
           
    }
    function sectionFocuse(e) {
        let target = e.currentTarget.parentNode;
        target.classList.add('focused');
    }

    function sectionBlur(e) {
        let target = e.currentTarget.parentNode;
        target.classList.remove('focused');
    }
}