console.log("JS connected correctly");
let g;
do {
    g = prompt("Enter the user's gender: (M/F)");
    if (g) g = g.trim().toLowerCase();

    const mVariants = ["m", "male", "boy"];
    const fVariants = ["f", "female", "girl"];

    if (mVariants.includes(g)) {
        g = "M";
    } else if (fVariants.includes(g)) {
        g = "F";
    } else {
        alert("Invalid value");
        g = "";  
    }

} while (g !== "M" && g !== "F")

let age = prompt("Enter age: ");
age = Number(age);

if ((g === "M" && age >= 67 ) || (g === "F" && age >=62)){
    console.log("You can retire");
} else {
    console.log("You still have to work");
}