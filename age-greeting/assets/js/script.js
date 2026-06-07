console.log("JS connected correctly");

let age = prompt("Enter the user's age: ");
age  = Number(age);

if (age < 18) {
    console.log("Hi");
} else if (age >= 60) {
    console.log("Greetings");
} else {
    console.log("Welcome");
}