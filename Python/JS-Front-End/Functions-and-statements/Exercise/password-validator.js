function solve(password) {

    function isValidLength(password) {
        return password.length >= 6 && password.length <= 10
    }

    function isAlphaNumeric(password) {
        let regex = /^[A-Za-z0-9]+$/gm;
        let isCorrect = regex.test(password);

        return isCorrect
    }

    function hasAtLeastTwoDigits(password) {

        let digitCounter = 0;

        for (const digit of password) {
            if (!isNaN(digit)) {
                digitCounter++;
            }
        }

        return digitCounter >= 2;

    }

    isValidLength = isValidLength(password);
    isAlphaNumeric = isAlphaNumeric(password);
    hasAtLeastTwoDigits = hasAtLeastTwoDigits(password);

    if (!isValidLength) {
        console.log("Password must be between 6 and 10 characters");
    }

    if (!isAlphaNumeric) {
        console.log("Password must consist only of letters and digits");
    }

    if (!hasAtLeastTwoDigits) {
        console.log("Password must have at least 2 digits");
    }

    if (isValidLength && isAlphaNumeric && hasAtLeastTwoDigits) {
        console.log("Password is valid")
    }

} 

solve('logIn');
solve('MyPass123');
solve('Pa$s$s');