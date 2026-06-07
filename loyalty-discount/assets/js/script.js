console.log("JS connected correctly");

let loyaltyCard = prompt("Do you have the loyalty card? (yes/no)");

loyaltyCard = loyaltyCard.trim().toLowerCase();

if (loyaltyCard === "yes" || loyaltyCard === "y") {
    loyaltyCard = 1;
} else {
    loyaltyCard = 0;
}

let price = prompt("Enter the product price: ");

if (loyaltyCard) {
    price = price * 0.9;
}

console.log("The price to pay is: ", price);