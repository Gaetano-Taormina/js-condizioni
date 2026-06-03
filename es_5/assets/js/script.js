console.log("JS collegato correttamente");

let eta = prompt("inserire l'età dell'utente: ") ;
eta  = Number(eta) ;

if (eta < 18) {
    console.log("Ciao") ;
} else if (eta >= 60) {
    console.log("Salve") ;
} else {
    console.log("Benvenuto") ;
} 