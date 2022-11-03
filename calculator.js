// A basic arithmetic calculator in javascript

// Accepting the operator to use
const operator = prompt('Choose an operator for your calculation from any of (+-*/): ');

// Accepting the numbers to use (Operands)
const num1 = parseFloat(prompt('Enter your first number: '));
const num2 = parseFloat(prompt('Enter your second number: '));

let result;

// Determining the result of the calculation using conditional statements
if (operator == '+') {
    result = num1 + num2;
}
else if (operator == '-') {
    result = num1 - num2;
}
else if (operator == '*') {
    result = num1 * num2;
}
else if (operator == '/') {
    result = num1 / num2;
}
else {
    console.log ("Invalid input");
}

// Displaying the output of the calculation
console.log(num1 + operator + num2 + ' = ' + result);