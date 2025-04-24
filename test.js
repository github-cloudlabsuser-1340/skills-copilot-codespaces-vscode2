// Calculator class to encapsulate operations
class Calculator {
    // Add two numbers
    add(a, b) {
        return a + b;
    }

    // Subtract two numbers
    subtract(a, b) {
        return a - b;
    }

    // Multiply two numbers
    multiply(a, b) {
        return a * b;
    }

    // Divide two numbers with error handling for division by zero
    divide(a, b) {
        if (b === 0) {
            return "Error! Division by zero.";
        }
        return a / b;
    }
}

// Main function to interact with the user
function main() {
    const calculator = new Calculator();
    console.log("Welcome to the Calculator!");

    const prompt = require("prompt-sync")(); // Use prompt-sync for user input

    while (true) {
        console.log("\nSelect an operation:");
        console.log("1. Add");
        console.log("2. Subtract");
        console.log("3. Multiply");
        console.log("4. Divide");
        console.log("5. Exit");

        const choice = prompt("Enter your choice (1/2/3/4/5): ").trim();

        if (choice === "5") {
            console.log("Thanks for using the calculator. Goodbye!");
            break;
        }

        const num1 = parseFloat(prompt("Enter the first number: "));
        const num2 = parseFloat(prompt("Enter the second number: "));

        let result;
        switch (choice) {
            case "1":
                result = calculator.add(num1, num2);
                console.log(`Result: ${result}`);
                break;
            case "2":
                result = calculator.subtract(num1, num2);
                console.log(`Result: ${result}`);
                break;
            case "3":
                result = calculator.multiply(num1, num2);
                console.log(`Result: ${result}`);
                break;
            case "4":
                result = calculator.divide(num1, num2);
                console.log(`Result: ${result}`);
                break;
            default:
                console.log("Invalid choice. Please try again.");
        }
    }
}

// Run the main function
main();