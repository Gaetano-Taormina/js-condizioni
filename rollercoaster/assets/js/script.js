console.log("JS connected correctly");

let age = prompt("Declare the user's age: ");
age = Number(age);

if (age < 14) {
    alert("Access Denied: user is too young");
} else {
    let height = prompt("Declare the user's height(cm): ");
    height = Number(height);
    if (height < 140){
        alert("Access Denied: user does not meet the requirements");
    } else {
        console.log("Have fun");
    }
}
