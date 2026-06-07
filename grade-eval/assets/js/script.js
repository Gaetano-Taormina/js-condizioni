console.log("JS connected correctly");

let n = prompt("Enter a number between 1 and 10: ");

while (n < 1 || n > 10 ) {
    alert("Error: Invalid value");
    n = prompt("Enter a number between 1 and 10: ");
}

n = Number(n);
if(n < 6){
    console.log("Insufficient");
} else if (n < 8 ){
    console.log("Sufficient");
} else if (n < 10){
    console.log("Good");
} else{
    console.log("Excellent");
}