// script.js
console.log("JS connected correctly");
let name;

do {
    name = prompt("Enter user's name: ");
    if (!name) {
        alert("You have not entered any name");
    }
} while (!name);

console.log("The user's name is: ", name);
