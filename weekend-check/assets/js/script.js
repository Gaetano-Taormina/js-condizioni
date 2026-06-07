console.log("JS connected correctly");

let day = prompt("Enter the day of the week: ");

day = day.trim().toLowerCase();

if (day == "saturday" || day == "sunday") {
    console.log("Have a good weekend");
} else {
    console.log("Have a good day at work");
}