console.log("JS collegato correttamente");

let età = prompt("inserire la propria età: ");

età = Number(età);
if (età > 18){
    console.log("Accesso consentito al locale");
} else {
    window.open('','self');
    window.close();
}


