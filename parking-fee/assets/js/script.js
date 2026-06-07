console.log("JS connected correctly");

let h = Number(prompt("Indicate how many hours you will stay in the parking lot: "));
let cost;

if (h > 5){
    cost = 15;
} else if (h > 2){
    cost = 10;
} else {
    cost = 5;
}

console.log("The amount due is: " + cost + " € ");