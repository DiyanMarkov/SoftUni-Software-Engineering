function inventory(array) {
    
    let heroes = [];

    for (const heroData of array) {
        let [heroName, level, items] = heroData.split(' / ');
        
        let hero = {
            heroName,
            level: Number(level),
            items
        }

        heroes.push(hero);
    }

    heroes.sort((a,b) => a.level - b.level)

    for (const hero of heroes) {
        console.log(`Hero: ${hero.heroName}`)
        console.log(`level => ${hero.level}`)
        console.log(`items => ${hero.items}`)
    }
}

inventory([
    'Isacc / 25 / Apple, GravityGun',
    'Derek / 12 / BarrelVest, DestructionSword',
    'Hes / 1 / Desolator, Sentinel, Antara'  
    ])