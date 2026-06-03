console.log("JS collegato correttamente");

let username = prompt("inserire l'username: ") ;
let password = prompt("inserire la password: ") ;

if( username == "admin" && password == "1234") {
    console.log("Login effettuato") ;
} else {
    alert("Credenziali errate") ;
}