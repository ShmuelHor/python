// הדפסה לחלונית מלמעלה
window.alert(`What's up man`);
const date = new Date();
console.log(date);
// הדפסה להערה 
console.log(`I like pizza`);
let username1 = "";
while(username1 === "" || username1 === null){
    username1 = window.prompt("entter a username:");
}
let username = "";

const decrease = document.getElementById("decrease");
const roll = document.getElementById("roll");
const reset = document.getElementById("reset");
const inceease = document.getElementById("inceease");
const countLabel = document.getElementById("countLabel");
let count = 0;

document.getElementById("mySubmit").onclick = function(){
    username = document.getElementById("mytext").value;
    document.getElementById("myH1").textContent = `Hello ${username}`;
    document.getElementById("P1").textContent = `How are you today?`;

    document.getElementById("footer").style.display = '';
    document.getElementById("usernameContainer").style.display = 'none';

    roll.onclick = function(){
        count = Math.floor(Math.random()*100)+1;
        countLabel.textContent = count;}

    inceease.onclick = function(){
        count++;
        countLabel.textContent = count;}

    decrease.onclick = function(){
        count--;
        countLabel.textContent = count;}
    
    reset.onclick = function(){
        count = 0;
        countLabel.textContent = count;}
}
let age;
// document.getElementById("Approval").onclick = function(){
//     age = document.getElementById("yourAge").value;
//     if(age >= 18){
//         console.log(`aaaaaaaaaaa`);
//     }
//     else{
//         console.log(`bbbbbbbb`);
//     }
// }
let day = 1;
switch(day){
    case 1:
        console.log(`uibrfuyrvbuy`);
        break
    case 2:
        console.log(`aaaaaa`);
        break
}
let aaa = "shmuelllllllll";
console.log(aaa.charAt(2));

function Watch(){
    let time = new Date();
    let Hours = time.getHours();
    const meridiem = Hours >= 12 ? "PM" : "AM";
    Hours = Hours >= 12 ? Hours - 12 : Hours;
    Hours = Hours.toString().padStart(2,0)
    let Minutes = time.getMinutes().toString().padStart(2,0);
    let Seconds = time.getSeconds().toString().padStart(2,0);
    console.log(Minutes);
    document.getElementById("myWath").textContent = `${Hours} : ${Minutes} : ${Seconds} ${meridiem}`;
}
Watch()
setInterval(Watch,1000)