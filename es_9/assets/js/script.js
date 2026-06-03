console.log("JS collegato correttamente");

let n = prompt("Inserire un numero tra 1 e 10: ") ;

while (n < 1 || n > 10 ) {
    alert("Errore:Valore non valido") ;
    n = prompt("Inserire un numero tra 1 e 10: ") ;
}

n = Number(n) ;
if(n < 6){
    console.log("Insufficiente") ;
} else if (n < 8 ){
    console.log("Sufficiente") ;
} else if (n < 10){
    console.log("Buono") ;
} else{
    console.log("Ottimo") ;
}