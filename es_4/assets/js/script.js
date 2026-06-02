console.log("JS collegato correttamente");

let eta = prompt("dichiarare l'età dell'utente: ") ;
eta = Number(eta) ;

if (eta<14) {
    alert("Accesso Negato: l'utente è troppo giovane") ;
} else {
    let h = prompt("dichiarare l'altezza dell'utente(cm): ") ;
    h = Number(h) ;
    if (h<140){
        alert("Accesso Negato: l'utente non rispetta i requisiti") ;
    } else {
        console.log("Buon divertimento");
    }
}
