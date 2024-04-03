function arrangeMeetings(array) {

    const obj = {};

    for (const person of array) {
        [day, personName] = person.split(' ');

        if (!obj.hasOwnProperty(day)) {
            obj[day] = personName;
            console.log(`Scheduled for ${day}`)

        } else {
            console.log(`Conflict on ${day}!`);
        }
    }

    for (const [key, value] of Object.entries(obj)) {
        console.log(`${key} -> ${value}`);
    }
}

arrangeMeetings(['Monday Peter', 'Wednesday Bill', 'Monday Tim', 'Friday Tim'])