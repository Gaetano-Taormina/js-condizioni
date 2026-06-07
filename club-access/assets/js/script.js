console.log("JS connected correctly");

let age = prompt("Enter your age: ");

age = Number(age);
if (age > 18){
    console.log("Access granted to the club");
} else {
    window.open('','self');
    window.close();
}
