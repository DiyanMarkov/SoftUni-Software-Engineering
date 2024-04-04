function solve(array) {
    let message = array.shift();

    let commandLine = array.shift();

    while (commandLine !== 'Buy') {

        command = commandLine.split('?');

        if (command[0] === 'TakeEven') {
            let newMessage = '';

            for (let i = 0; i < message.length; i++) {
                
                if (i % 2 === 0) {
                    newMessage += message[i];
                }
                
            }

            message = newMessage;
            newMessage = '';
            console.log(message);

        } else if (command[0] === 'ChangeAll') {
            
            let substring = command[1];
            let replacement = command[2];

            if (message.includes(substring)) {
                while (message.includes(substring)) {
                    message = message.replace(substring, replacement);
                }
    
            }

            console.log(message);

        } else if (command[0] === 'Reverse') {
            let substr = command[1];

            if (message.includes(substr)) {
                message = message.replace(substr,'')

                let newSubstring = substr.split('').reverse().join('');
                message = message + newSubstring;
                console.log(message);
            } else {
                console.log('error');
            }
    

        }
        

        commandLine = array.shift();
    }
    
    console.log(`The cryptocurrency is: ${message}`)
}

solve(([
    "z2tdsfndoctsB6z7tjc8ojzdngzhtjsyVjek!snfzsafhscs",
    "TakeEven",
    "Reverse?!nzahc",
    "ChangeAll?m?g",
    "Reverse?adshk",
    "ChangeAll?z?i",
    "Buy"
])
)