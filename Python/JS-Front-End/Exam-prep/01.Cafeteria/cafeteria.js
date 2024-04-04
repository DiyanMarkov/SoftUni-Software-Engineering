function solve(array) {
    let countOfTimes = array.shift();

    let baristas = {};

    for (let i = 0; i < countOfTimes; i++) {

        let [name, shift, drinks] = array.shift().split(' ');
        
        drinks = drinks.split(',')

        baristas[name] = {
            shift,
            drinks
        }
    }


    let commandLine = array.shift();

    while (commandLine !== 'Closed') {
        
        let command = commandLine.split(' / ')

        switch (command[0]) {
            case 'Prepare':
                
                if (baristas[command[1]].shift === command[2] && baristas[command[1]].drinks.includes(command[3])) {
                    console.log(`${command[1]} has prepared a ${command[3]} for you!`);
                } else {
                    console.log(`${command[1]} is not available to prepare a ${command[3]}.`);
                }
                
                break;

            case 'Change Shift':

                baristas[command[1]].shift = command[2];
                console.log(`${command[1]} has updated his shift to: ${command[2]}`);

                break;

            case 'Learn':
                
                if (baristas[command[1]].drinks.includes(command[2])) {
                    console.log(`${command[1]} knows how to make ${command[2]}.`);
                } else {
                    baristas[command[1]].drinks.push(command[2]);
                    console.log(`${command[1]} has learned a new coffee type: ${command[2]}.`);
                }

                break;
            
        }

        commandLine = array.shift();
    }

    for (const barista in baristas) {
        allDrinks = baristas[barista].drinks.join(', ');
        console.log(`Barista: ${barista}, Shift: ${baristas[barista].shift}, Drinks: ${allDrinks}`);
    }

}

solve([
    '3',
      'Alice day Espresso,Cappuccino',
      'Bob night Latte,Mocha',
      'Carol day Americano,Mocha',
      'Prepare / Alice / day / Espresso',
      'Change Shift / Bob / night',
      'Learn / Carol / Latte',
      'Learn / Bob / Latte',
      'Prepare / Bob / night / Latte',
      'Closed']
    
    );