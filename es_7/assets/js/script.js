console.log("JS collegato correttamente");

let g = prompt("inserire il giorno della settimana: ") ;

g = g.trim().toLowerCase() ;

if (g == "sabato" || g == "domenica") {
    console.log("Buon weekend") ;
} else {
    console.log("Buon lavoro") ;
}