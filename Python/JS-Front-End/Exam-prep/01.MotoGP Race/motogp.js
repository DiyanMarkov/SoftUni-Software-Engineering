function solve(array) {
    const countTimes = Number(array.shift());
    
    let riders = {}

    for (let i = 0; i < countTimes; i++) {
        let [name, fuel, position] = array.shift().split('|');
        
        riders[name] = { 
            fuel: Number(fuel),
            position: Number(position) 
        }
    }

    let commandLine = array.shift();

    while (commandLine !== 'Finish') {

        let command = commandLine.split(' - ')

        switch (command[0]) {
            case 'StopForFuel':

                let currentCommand = command.shift();
                let riderName = command.shift();
                let minimumFuel = Number(command.shift());
                let changedPosition = Number(command.shift());

                

                if (riders[riderName].fuel < minimumFuel) {
                    riders[riderName].position = changedPosition;
                    console.log(`${riderName} stopped to refuel but lost his position, now he is ${changedPosition}.`);
                } else {
                    console.log(`${riderName} does not need to stop for fuel!`);
                }

                break;

            case 'Overtaking':
    
                let firstRider = command[1];
                let secondRider = command[2];

                firstRiderPosition = riders[firstRider].position;
                secondRiderPosition = riders[secondRider].position;

                if (firstRiderPosition < secondRiderPosition) {

                    riders[secondRider].position = firstRiderPosition;
                    riders[firstRider].position = secondRiderPosition;

                    console.log(`${firstRider} overtook ${secondRider}!`);
                }

                break;

            case 'EngineFail':

                let rider = command[1];
                let lapsLeft = command[2];

                delete riders[rider];

                console.log(`${rider} is out of the race because of a technical issue, ${lapsLeft} laps before the finish.`);

                break;
        }

        commandLine = array.shift();
    }

    for (const rider in riders) {

        console.log(`${rider}`)
        console.log(`  Final position: ${riders[rider].position}`);
    }

}

solve((["4",
"Valentino Rossi|100|1",
"Marc Marquez|90|3",
"Jorge Lorenzo|80|4",
"Johann Zarco|80|2",
"StopForFuel - Johann Zarco - 90 - 5",
"Overtaking - Marc Marquez - Jorge Lorenzo",
"EngineFail - Marc Marquez - 10",
"Finish"])

)