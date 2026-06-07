console.log("JS connected correctly");

let ticketPrice = 36;
let luggageWeight = prompt("Enter your luggage weight in kg");

luggageWeight = Number(luggageWeight);

if (luggageWeight > 23) {
    ticketPrice = ticketPrice + 20;
}

console.log(`The ticket price is ${ticketPrice}`);