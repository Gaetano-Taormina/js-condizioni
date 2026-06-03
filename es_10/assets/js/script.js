console.log("JS collegato correttamente");

let h = Number(prompt("Indica per quante ore resterai nel parcheggio: ")) ;
let costo ;

if (h > 5){
    costo = 15 ;
} else if (h > 2){
    costo = 10 ;
} else {
    costo = 5 ;
}

console.log("la cifra dovuta è: " + costo + " € ") ;