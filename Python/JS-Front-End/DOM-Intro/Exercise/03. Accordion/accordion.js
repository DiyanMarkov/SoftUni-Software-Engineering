function toggle() {
    let button = document.getElementsByClassName('button')[0];
    let extraInfo = document.getElementById('extra');

    if (button.textContent === 'More') {
        extraInfo.style.display = 'block';
        button.textContent = 'Less';
    } else if (button.textContent === 'Less') {
        extraInfo.style.display = 'none';
        button.textContent = 'More';
    }
    
    console.log(button);
}