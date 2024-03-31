function divideFactorials (num1, num2) {

    function factorial(n) { 
        if (n === 0 || n === 1) { 
            return 1; 
        } else { 
            return n * factorial(n - 1); 
        } 
    }

    let firstFactorial = factorial(num1);
    let secondFactorial = factorial(num2);

    result = firstFactorial / secondFactorial

    console.log(result.toFixed(2));
}

divideFactorials(5, 2)