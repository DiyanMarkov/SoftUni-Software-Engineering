function solve(speed, area) {
    const motorwayLimit = 130
    const interstateLimit = 90
    const cityLimit = 50
    const residentialAreaLimit = 20

    let result;
    let difference = 0;

    if (area === 'motorway') {

        if (speed > motorwayLimit) {

            if (speed - motorwayLimit <= 20) {
                difference = speed - motorwayLimit
                result = `The speed is ${difference} km/h faster than the allowed speed of ${motorwayLimit} - speeding`;

            } else if (speed - motorwayLimit <= 40) {
                difference = speed - motorwayLimit
                result = `The speed is ${difference} km/h faster than the allowed speed of ${motorwayLimit} - excessive speeding`;
            } else {
                difference = speed - motorwayLimit
                result = `The speed is ${difference} km/h faster than the allowed speed of ${motorwayLimit} - reckless driving`;
            } 

        } else {
            result = `Driving ${speed} km/h in a ${motorwayLimit} zone`
        }

    } else if (area === 'interstate') {

        if (speed > interstateLimit) {

            if (speed - interstateLimit <= 20) {
                difference = speed - interstateLimit
                result = `The speed is ${difference} km/h faster than the allowed speed of ${interstateLimit} - speeding`;

            } else if (speed - interstateLimit <= 40) {
                difference = speed - interstateLimit
                result = `The speed is ${difference} km/h faster than the allowed speed of ${interstateLimit} - excessive speeding`;
            } else {
                difference = speed - interstateLimit
                result = `The speed is ${difference} km/h faster than the allowed speed of ${interstateLimit} - reckless driving`;
            } 

        } else {
            result = `Driving ${speed} km/h in a ${interstateLimit} zone`
        }

    } else if (area === 'city') {

        if (speed > cityLimit) {

            if (speed - cityLimit <= 20) {
                difference = speed - cityLimit
                result = `The speed is ${difference} km/h faster than the allowed speed of ${cityLimit} - speeding`;

            } else if (speed - cityLimit <= 40) {
                difference = speed - cityLimit
                result = `The speed is ${difference} km/h faster than the allowed speed of ${cityLimit} - excessive speeding`;
            } else {
                difference = speed - cityLimit
                result = `The speed is ${difference} km/h faster than the allowed speed of ${cityLimit} - reckless driving`;
            } 

        } else {
            result = `Driving ${speed} km/h in a ${cityLimit} zone`
        }

    } else if (area === 'residential') {

        if (speed > residentialAreaLimit) {

            if (speed - residentialAreaLimit <= 20) {
                difference = speed - residentialAreaLimit
                result = `The speed is ${difference} km/h faster than the allowed speed of ${residentialAreaLimit} - speeding`;

            } else if (speed - residentialAreaLimit <= 40) {
                difference = speed - residentialAreaLimit
                result = `The speed is ${difference} km/h faster than the allowed speed of ${residentialAreaLimit} - excessive speeding`;
            } else {
                difference = speed - residentialAreaLimit
                result = `The speed is ${difference} km/h faster than the allowed speed of ${residentialAreaLimit} - reckless driving`;
            } 

        } else {
            result = `Driving ${speed} km/h in a ${residentialAreaLimit} zone`
        }

    } 

    console.log(result);
}

solve(40, 'city');
solve(200, 'motorway');
solve(21, 'residential');
solve(120, 'interstate');
