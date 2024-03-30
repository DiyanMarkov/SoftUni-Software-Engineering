function attachEventsListeners() {
    let daysInput = document.getElementById('days');
    let daysBtn = document.getElementById('daysBtn');

    let hoursInput = document.getElementById('hours');
    let hoursBtn = document.getElementById('hoursBtn');

    let minutesInput = document.getElementById('minutes');
    let minutesBtn = document.getElementById('minutesBtn');

    let secondsInput = document.getElementById('seconds');
    let secondsBtn = document.getElementById('secondsBtn');

    daysBtn.addEventListener('click', days);
    hoursBtn.addEventListener('click', hours);
    minutesBtn.addEventListener('click', minutes);
    secondsBtn.addEventListener('click', seconds);

    function days(e) {
        hoursInput.value = daysInput.value * 24;
        minutesInput.value = hoursInput.value * 60;
        secondsInput.value = minutesInput.value * 60;
    }
    
    function hours(e) {
        daysInput.value = hoursInput.value / 24;
        minutesInput.value = hoursInput.value * 60;
        secondsInput.value = minutesInput.value * 60;
    }

    function minutes(e) {
        hoursInput.value = minutesInput.value / 60;
        daysInput.value = hoursInput.value / 24
        secondsInput.value = minutesInput.value * 60;
    }

    function seconds(e) {
        minutesInput.value = secondsInput.value / 60;
        hoursInput.value = minutesInput.value / 60;
        daysInput.value = hoursInput.value / 24;
    }
    
}