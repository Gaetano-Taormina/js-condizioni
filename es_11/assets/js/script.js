console.log("JS collegato correttamente");
let g;
do {
    g = prompt("Inserire il gender dell'utente: (M/F)") ;
    g = g.trim().toLowerCase();

    const M_Variants = ["m", "maschio", "male"];
    const F_Variants = ["f", "femmina", "female"];

    if (M_Variants.includes(g)) {
        g = "M";
    } else if (F_Variants.includes(g)) {
        g = "F";
    } else {
        alert("Valore non valido");
        g = "";  
    }

} while (g !== "M" && g !== "F")

let eta = prompt("Inserire eta: ");
eta = Number(eta);

if ((g === "M" && eta >= 67 ) || (g === "F" && eta >=62)){
    console.log("Puoi andare in pensione");
} else {
    console.log("Devi ancora lavorare");
}