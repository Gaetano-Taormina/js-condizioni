// script.js
console.log ("funziona") ;
let nome ;

do {
    nome = prompt ("inserire il tuo nome: ") ;
    if (!nome) {
        alert ("non hai inserito nessun nome") ;
    }
} while (!nome) ;

console.log ("il nome dell'utente è: ", nome) ;

