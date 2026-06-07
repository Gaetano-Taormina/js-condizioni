console.log("JS connected correctly");

let username = prompt("Enter username: ");
let password = prompt("Enter password: ");

if( username == "admin" && password == "1234") {
    console.log("Login successful");
} else {
    alert("Invalid credentials");
}