function attachGradientEvents() {
    let gradient = document.getElementById('gradient');
    let result = document.getElementById('result');

    gradient.addEventListener('mousemove', gradientMove);
    gradient.addEventListener('mouseout', gradientOut);

    function gradientMove(e) {
        // Calculate the relative position of the mouse cursor within the 'gradient' element
        // by dividing the horizontal offset of the cursor by the total width
        let power = e.offsetX / (e.target.clientWidth - 1);
        // Convert the relative position to a percentage by multiplying it with 100
        power = Math.trunc(power * 100);
        result.textContent = power + '%';
    }

    function gradientOut(e) {
        result.textContent = '';
    }
}