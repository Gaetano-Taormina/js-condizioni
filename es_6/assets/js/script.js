console.log("JS collegato correttamente");

let tessera = prompt ("Hai la tessera? (si/no)") ;

tessera = tessera.trim().toLowerCase() ;

if (tessera === "si") {
    tessera = 1 ;
} else {
    tessera = 0 ;
}

let prezzo = prompt("Inserire il prezzo del prodotto: ") ;

if (tessera) {
    prezzo = prezzo * 0.9 ;
}

console.log("Il prezzo da pagare è: ", prezzo)