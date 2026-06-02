console.log("JS collegato correttamente");

let Prezzo_Biglietto = 36 ;
let Peso_Valigia = prompt ("Inserire il peso della propria valigia in kg") ;

Peso_Valigia = Number (Peso_Valigia) ;

if (Peso_Valigia > 23) {
    Prezzo_Biglietto = Prezzo_Biglietto + 20 ;
}

console.log(`il prezzo del biglietto è ${Prezzo_Biglietto}`) ;