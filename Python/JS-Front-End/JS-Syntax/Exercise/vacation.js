function calculate(people, group, day) {

    let total;

    if (group === 'Students') {

        if (day === 'Friday') {
            total = people * 8.45
        } else if (day === 'Saturday') {
            total = people * 9.80
        } else if (day === 'Sunday') {
            total = people * 10.46
        }

        if (people >=30) {
            total *= 0.85
        }

    } else if (group === 'Business') {

        let price;

        if (day === 'Friday') {
            price = 10.90
            total = people * price
        } else if (day === 'Saturday') {
            price = 15.60
            total = people * price
        } else if (day === 'Sunday') {
            price = 16
            total = people * price
        }

        if (people >=100) {
            total -= 10 * price
        }

    }  else if (group === 'Regular') {
        if (day === 'Friday') {
            total = people * 15
        } else if (day === 'Saturday') {
            total = people * 20
        } else if (day === 'Sunday') {
            total = people * 22.50
        }

        if (people >=10 && people <= 20) {
            total *= 0.95
        }
    
    }

    console.log(`Total price: ${total.toFixed(2)}`)
}

calculate(30,"Students","Sunday")
calculate(40,"Regular","Saturday")

