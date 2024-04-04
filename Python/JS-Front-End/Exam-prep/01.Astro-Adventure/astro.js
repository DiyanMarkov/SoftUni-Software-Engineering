function solve(array) {
    let count = Number(array.shift());

    let astronauts = {};

    for (let i = 0; i < count; i++) {
        let currentAstronaut = array.shift();
        let [name, oxygenLevel, energyReserve] = currentAstronaut.split(' ')
        
        astronauts[name] = {
            oxygenLevel: Number(oxygenLevel),
            energyReserve: Number(energyReserve)
        }
    }

    let commandLine = array.shift();

    while (commandLine !== 'End') {

        let command = commandLine.split(' - ');

        if (command[0] === 'Explore') {

            let name = command[1];
            let energyNeeded = Number(command[2]);

            if (astronauts[name].energyReserve >= energyNeeded) {
                astronauts[name].energyReserve -= energyNeeded

                console.log(`${name} has successfully explored a new area and now has ${astronauts[name].energyReserve} energy!`);
            } else {
                console.log(`${name} does not have enough energy to explore!`);
            }

        } else if (command[0] === 'Refuel') {

            let astroName = command[1];
            let refuelAmount = Number(command[2]);

            let recoveredEnergy = refuelAmount;

            if (astronauts[astroName].energyReserve + refuelAmount> 200) {
                recoveredEnergy = 200 - astronauts[astroName].energyReserve
                astronauts[astroName].energyReserve = 200;
            } else {
                astronauts[astroName].energyReserve += refuelAmount;
            }

            

            console.log(`${astroName} refueled their energy by ${recoveredEnergy}!`);

        }  else if (command[0] === 'Breathe') {
            let astroName = command[1];
            let breathReplenishAmount = Number(command[2]);

            let recoveredOxygen = breathReplenishAmount;

            if (astronauts[astroName].oxygenLevel + breathReplenishAmount > 100) {
                recoveredOxygen = 100 - astronauts[astroName].oxygenLevel;
                astronauts[astroName].oxygenLevel = 100;
            } else {
                astronauts[astroName].oxygenLevel += breathReplenishAmount;
            }

            console.log(`${astroName} took a breath and recovered ${recoveredOxygen} oxygen!`);
        }  

        commandLine = array.shift()
    }

    for (const astronaut in astronauts) {
        console.log(`Astronaut: ${astronaut}, Oxygen: ${astronauts[astronaut].oxygenLevel}, Energy: ${astronauts[astronaut].energyReserve}`);
    }

}


solve([    '4',
'Alice 60 100',
'Bob 40 80',
'Charlie 70 150',
'Dave 80 180',
'Explore - Bob - 60',
'Refuel - Alice - 30',
'Breathe - Charlie - 50',
'Refuel - Dave - 40',
'Explore - Bob - 40',
'Breathe - Charlie - 30',
'Explore - Alice - 40',
'End']

)