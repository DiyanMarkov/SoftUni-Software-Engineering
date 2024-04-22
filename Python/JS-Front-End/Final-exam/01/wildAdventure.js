function solve(array) {
    let count = array.shift()

    let people = {};

    for (let i = 0; i < count; i++) {
        let [name, hp, bullets] = array.shift().split(' ');

        people[name] = {
            hp: Number(hp),
            bullets: Number(bullets)
        }
    }

    let consoleLine = array.shift().split(' - ')

    while (consoleLine[0] !== 'Ride Off Into Sunset') {

        let command = consoleLine;

        if (command[0] === 'FireShot') {

            let name = command[1];
            let target = command[2];

            if (people[name].bullets > 0) {
                people[name].bullets -= 1;
                let bulletsLeft = people[name].bullets

                console.log(`${name} has successfully hit ${target} and now has ${bulletsLeft} bullets!`);

            } else {
                console.log(`${name} doesn't have enough bullets to shoot at ${target}!`);
            }

        } else if (command[0] === 'TakeHit') {

            let character = command[1];
            let damage = Number(command[2]);
            let attacker = command[3];

            people[character].hp -= damage

            let hpLeft = people[character].hp

            if (people[character].hp > 0) {

                console.log(`${character} took a hit for ${damage} HP from ${attacker} and now has ${hpLeft} HP!`);

            } else {
                delete people[character]
                console.log(`${character} was gunned down by ${attacker}!`);
            }

        } else if (command[0] === 'Reload') {

            let character = command[1];

            if (people[character].bullets < 6) {
                let bulletsToFull = 6 - people[character].bullets
                people[character].bullets = 6
                console.log(`${character} reloaded ${bulletsToFull} bullets!`);
            } else {
                console.log(`${character}'s pistol is fully loaded!`);
            }

        } else if (command[0] === 'PatchUp') {

            let character = command[1];
            let healAmount = Number(command[2]);

            if (people[character].hp === 100) {

                console.log(`${character} is in full health!`);

            } else {

                if (people[character].hp + healAmount > 100) {

                    let healed = 100 - people[character].hp;
                    people[character].hp = 100;
                    console.log(`${character} patched up and recovered ${healed} HP!`);

                } else if (people[character].hp + healAmount <= 100) {
                    people[character].hp += healAmount
                    console.log(`${character} patched up and recovered ${healAmount} HP!`);
                }

                

            } 
        }

        consoleLine = array.shift().split(' - ')
    }

    for (const person in people) {
        console.log(`${person}`);
        console.log(`  HP: ${people[person].hp}`);
        console.log(`  Bullets: ${people[person].bullets}`);
    }

}

solve((["2",
"Gus 100 0",
"Walt 100 6",
"FireShot - Gus - Bandit",
"TakeHit - Gus - 100 - Bandit",
"Reload - Walt",
"Ride Off Into Sunset"])

)

